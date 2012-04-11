from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from charts.cms_plugin.models import ChartPluginModel

class ChartPlugin(CMSPluginBase):
    model = ChartPluginModel
    name = _("Chart Plugin") # Name of the plugin
    render_template = "charts/render_chart.html"

    def render(self, context, instance, placeholder):
        context['chart'] = instance
        return context

plugin_pool.register_plugin(ChartPlugin)