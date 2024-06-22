# coding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtDesigner import QDesignerCustomWidgetInterface

from qfluentwidgets import (BodyLabel, CaptionLabel, StrongBodyLabel, SubtitleLabel, TitleLabel, LargeTitleLabel,
                            DisplayLabel, ImageLabel, AvatarWidget, HyperlinkLabel)

from plugin_base import PluginBase


class LabelPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Label)'

    def domXml(self):
        return f"""
        <widget class="{self.name()}" name="{self.name()}">
            <property name="text">
                <string>{self.toolTip()}</string>
            </property>
        </widget>
        """


class CaptionLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Caption label plugin """

    def createWidget(self, parent):
        return CaptionLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "CaptionLabel"


class BodyLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Body label plugin """

    def createWidget(self, parent):
        return BodyLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "BodyLabel"


class StrongBodyLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Strong body label plugin """

    def createWidget(self, parent):
        return StrongBodyLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "StrongBodyLabel"


class SubtitleLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Subtitle label plugin """

    def createWidget(self, parent):
        return SubtitleLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "SubtitleLabel"


class TitleLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Title label plugin """

    def createWidget(self, parent):
        return TitleLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "TitleLabel"


class LargeTitleLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Title label plugin """

    def createWidget(self, parent):
        return LargeTitleLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "LargeTitleLabel"


class DisplayLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Display label plugin """

    def createWidget(self, parent):
        return DisplayLabel(parent)

    def icon(self):
        return super().icon("TextBlock")

    def name(self):
        return "DisplayLabel"


class HyperlinkLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Hyperlink label plugin """

    def createWidget(self, parent):
        return HyperlinkLabel(parent)

    def icon(self):
        return super().icon("HyperlinkButton")

    def name(self):
        return "HyperlinkLabel"


class ImageLabelPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Image label plugin """

    def createWidget(self, parent):
        return ImageLabel(self.icon().pixmap(72, 72), parent)

    def icon(self):
        return super().icon("Image")

    def name(self):
        return "ImageLabel"

    def domXml(self):
        return f"""<widget class="{self.name()}" name="{self.name()}"></widget>"""


class AvatarPlugin(LabelPlugin, QDesignerCustomWidgetInterface):
    """ Avatar plugin """

    def createWidget(self, parent):
        return AvatarWidget(self.icon().pixmap(72, 72), parent)

    def icon(self):
        return super().icon("PersonPicture")

    def name(self):
        return "AvatarWidget"

    def domXml(self):
        return f"""<widget class="{self.name()}" name="{self.name()}"></widget>"""
