class DataMixin:
    paginate_by = 3
    def get_user_data(self, **kwargs):
        context = kwargs
        return context
