from django.views import generic
from .forms import InquiryForm
logger=logging.getLogger(__name__)

# Create your views here.

class IndexView(generic.TemplateView):
    template_name="index.html"


class TestView(generic.TemplateView):
    template_name="test.html"

class InquiryView(generic.FormView):
    template_name="inquiry.html"
    form_class=InquiryForm