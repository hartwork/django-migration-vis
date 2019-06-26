from django.core.management.base import BaseCommand
from django.db.migrations.loader import MigrationLoader
from graphviz import Digraph
from tempfile import NamedTemporaryFile


class Command(BaseCommand):

    def handle(self, *apps, **options):
        self.graph = MigrationLoader(None).graph
        comment = options['comment']
        self.picture = Digraph(comment=comment)
        save_loc = options['filename']
        self.render(save_loc)

    def add_arguments(self, parser):
        parser.add_argument('--comment',
                            help='optional comments/captions for the picture')
        parser.add_argument('filename', nargs='?',
                            help='a filename to write GraphViz contents to')

    def _create_digraph(self):
        nodes = sorted(self.graph.nodes.values(),
                       key=self._get_tuple)
        for node in nodes:
            self._add_node(node)
        for node in nodes:
            self._add_dependencies(node)

    # @staticmethod
    def _style_label(self, tupled_node):
        return '/'.join(tupled_node)

    @staticmethod
    def _get_tuple(node):
        return (node.app_label, node.name)

    def _add_node(self, node):
        node_label = self._style_label(self._get_tuple(node))
        self.picture.node(node_label, node_label)

    def _add_edges(self, nodeTo, nodeFrom):
        self.picture.edge(self._style_label(nodeFrom),
                          self._style_label(nodeTo))

    def _add_dependencies(self, node):
        for dep in node.dependencies:
            if dep[1] == '__first__':
                self._add_edges(self.graph.root_nodes(dep[0])[0],
                                self._get_tuple(node))
            elif dep[1] == '__latest__':
                self._add_edges(self.graph.leaf_nodes(dep[0])[0],
                                self._get_tuple(node))
            else:
                self._add_edges(dep, self._get_tuple(node))

    def render(self, save_loc):
        self._create_digraph()
        if save_loc:
            self.picture.render(save_loc, view=False)
        else:
            with NamedTemporaryFile() as temp:
                self.picture.render(temp.name, view=True)
