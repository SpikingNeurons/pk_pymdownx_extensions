from pymdownx.blocks import BlocksExtension
from pymdownx.blocks.block import Block
import xml.etree.ElementTree as etree

class MyBlock(Block):
    NAME = 'my-block'

    def on_create(self, parent):

        return etree.SubElement(parent, 'div')


class MyBlockExtension(BlocksExtension):

    def extendMarkdownBlocks(self, md, block_mgr):

        block_mgr.register(MyBlock, self.getConfigs())


def makeExtension(*args, **kwargs):
    """Return extension."""

    return MyBlockExtension(*args, **kwargs)