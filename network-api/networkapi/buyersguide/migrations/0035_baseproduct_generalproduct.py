# Generated by Django 2.2.12 on 2020-04-13 19:08

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import networkapi.buyersguide.fields
import networkapi.buyersguide.pagemodels.get_product_image_upload_path


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0034_auto_20200113_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft', models.BooleanField(default=True, help_text='When checked, this product will only show for CMS-authenticated users')),
                ('adult_content', models.BooleanField(default=False, help_text='When checked, product thumbnail will appear blurred as well as have an 18+ badge on it')),
                ('review_date', models.DateField(help_text='Review date of this product')),
                ('name', models.CharField(blank=True, help_text='Name of Product', max_length=100)),
                ('slug', models.CharField(blank=True, default=None, editable=False, help_text='slug used in urls', max_length=256)),
                ('company', models.CharField(blank=True, help_text='Name of Company', max_length=100)),
                ('blurb', models.TextField(blank=True, help_text='Description of the product', max_length=5000)),
                ('url', models.URLField(blank=True, help_text='Link to this product page', max_length=2048)),
                ('price', models.CharField(blank=True, help_text='Price', max_length=100)),
                ('image', models.FileField(blank=True, help_text='Image representing this product', max_length=2048, upload_to=networkapi.buyersguide.pagemodels.get_product_image_upload_path.get_product_image_upload_path)),
                ('cloudinary_image', cloudinary.models.CloudinaryField(blank=True, help_text='Image representing this product - hosted on Cloudinary', max_length=255, verbose_name='image')),
                ('meets_minimum_security_standards', models.BooleanField(help_text='Does this product meet minimum security standards?', null=True)),
                ('uses_encryption', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does the product use encryption?')),
                ('uses_encryption_helptext', models.TextField(blank=True, max_length=5000)),
                ('security_updates', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Security updates?')),
                ('security_updates_helptext', models.TextField(blank=True, max_length=5000)),
                ('strong_password', networkapi.buyersguide.fields.ExtendedYesNoField()),
                ('strong_password_helptext', models.TextField(blank=True, max_length=5000)),
                ('manage_vulnerabilities', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Manages security vulnerabilities?')),
                ('manage_vulnerabilities_helptext', models.TextField(blank=True, max_length=5000)),
                ('privacy_policy', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product have a privacy policy?')),
                ('privacy_policy_helptext', models.TextField(blank=True, max_length=5000)),
                ('share_data', models.BooleanField(help_text='Does the maker share data with other companies?', null=True)),
                ('share_data_helptext', models.TextField(blank=True, max_length=5000)),
                ('how_does_it_share', models.CharField(blank=True, help_text='How does this product handle data?', max_length=5000)),
                ('user_friendly_privacy_policy', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product have a user-friendly privacy policy?')),
                ('user_friendly_privacy_policy_helptext', models.TextField(blank=True, max_length=5000)),
                ('worst_case', models.CharField(blank=True, help_text="What's the worst thing that could happen by using this product?", max_length=5000)),
                ('phone_number', models.CharField(blank=True, help_text='Phone Number', max_length=100)),
                ('live_chat', models.CharField(blank=True, help_text='Live Chat', max_length=100)),
                ('email', models.CharField(blank=True, help_text='Email', max_length=100)),
                ('twitter', models.CharField(blank=True, help_text='Twitter username', max_length=100)),
                ('product_category', models.ManyToManyField(blank=True, related_name='pniproduct', to='buyersguide.BuyersGuideProductCategory')),
                ('related_products', models.ManyToManyField(blank=True, related_name='related_pniproduct', to='buyersguide.BaseProduct')),
                ('updates', models.ManyToManyField(blank=True, related_name='pniproduct', to='buyersguide.Update')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BaseProductPrivacyPolicyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('label', models.CharField(help_text='Label for this link on the product page', max_length=500)),
                ('url', models.URLField(blank=True, help_text='Privacy policy URL', max_length=2048)),
                ('product', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='privacy_policy_links', to='buyersguide.BaseProduct')),
            ],
            options={
                'verbose_name': 'Buyers Guide Product Privacy Policy link',
                'verbose_name_plural': 'Buyers Guide Product Privacy Policy links',
            },
        ),
        migrations.CreateModel(
            name='GeneralProduct',
            fields=[
                ('baseproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='buyersguide.BaseProduct')),
                ('camera_device', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this device have or access a camera?')),
                ('camera_app', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does the app have or access a camera?')),
                ('microphone_device', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this Device have or access a microphone?')),
                ('microphone_app', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this app have or access a microphone?')),
                ('location_device', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product access your location?')),
                ('location_app', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this app access your location?')),
                ('delete_data', models.BooleanField(help_text='Can you request data be deleted?', null=True)),
                ('delete_data_helptext', models.TextField(blank=True, max_length=5000)),
                ('parental_controls', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Are there rules for children?', null=True)),
                ('child_rules_helptext', models.TextField(blank=True, max_length=5000)),
                ('collects_biometrics', networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product collect biometric data?')),
                ('collects_biometrics_helptext', models.TextField(blank=True, max_length=5000)),
            ],
            options={
                'abstract': False,
            },
            bases=('buyersguide.baseproduct',),
        ),
        migrations.CreateModel(
            name='SoftwareProduct',
            fields=[
                ('baseproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='buyersguide.BaseProduct')),
            ],
            options={
                'abstract': False,
            },
            bases=('buyersguide.baseproduct',),
        ),
    ]
