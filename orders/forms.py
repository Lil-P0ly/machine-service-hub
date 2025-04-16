from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    
    # requires_delivery = forms.ChoiceField(
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #         ],
    #     )
    organisation_info = forms.CharField(required=False)
    # delivery_address = forms.CharField(required=False)
    # payment_on_get = forms.ChoiceField(
    #     choices=[
    #         ("0", 'False'),
    #         ("1", 'True'),
    #         ],
    #     )
