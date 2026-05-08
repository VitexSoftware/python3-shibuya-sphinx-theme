from docutils import nodes
from sphinx import addnodes
from sphinx.transforms.post_transforms import SphinxPostTransform


class WrapperPostTransform(SphinxPostTransform):
    formats = ("html",)
    default_priority = 500

    def _findall(self, node_class):
        """Compatible findall for docutils < 0.18 (which lacks findall)."""
        if hasattr(self.document, 'findall'):
            return self.document.findall(node_class)
        return self.document.traverse(node_class)

    def run(self, **kwargs) -> None:
        """Perform the post-transform on `self.document`."""
        elements = self._findall(nodes.table)
        self._wrap(elements, "table-wrapper")

        elements = self._findall(nodes.math_block)
        self._wrap(elements, "math-wrapper")

        elements = self._findall(addnodes.toctree)
        for el in elements:
            el["titlesonly"] = True

    @staticmethod
    def _wrap(elements, classname: str):
        for node in list(elements):
            new_node = nodes.container(classes=[classname])
            new_node.update_all_atts(node)
            node.parent.replace(node, new_node)
            new_node.append(node)
