# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import v1.blocks
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0126_add_conf_reg_answer_id_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'bureau_structure', wagtail.wagtailcore.blocks.StructBlock([(b'last_updated_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'download_image', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon=b'image')), (b'director', wagtail.wagtailcore.blocks.CharBlock()), (b'divisions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'division', v1.blocks.PlaceholderCharBlock(label=b'Division')), (b'division_lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))])), (b'division_lead_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Name', label=b'Division Lead')), (b'title_1', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))], label=b'Title')), (b'link_to_division_page', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'offices', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'office_name', wagtail.wagtailcore.blocks.CharBlock()), (b'lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))]))], required=False)))]))), (b'office_of_the_director', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'office_name', wagtail.wagtailcore.blocks.CharBlock()), (b'lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))])), (b'offices', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'office_name', wagtail.wagtailcore.blocks.CharBlock()), (b'lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))]))], required=False)))]), label=b'Office of the Director'))])), (b'info_unit_group', wagtail.wagtailcore.blocks.StructBlock([(b'format', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Choose the number and width of info unit columns.', choices=[(b'50-50', b'50/50'), (b'33-33-33', b'33/33/33'), (b'25-75', b'25/75')], label=b'Format')), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'If this field is not empty, the Heading field must also be set.', required=False)), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", default=True, required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of info unit group.', default=False, required=False)), (b'lines_between_items', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to show horizontal rule lines between info units.', default=False, required=False, label=b'Show rule lines between items')), (b'info_units', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], default={b'level': b'h3'}, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))]))), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', required=False, label=b'Include sharing links?')), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', required=False, label=b'ID for this content block'))]))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'full', b'full'), (470, b'470px'), (270, b'270px'), (170, b'170px')])), (b'image_position', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Does not apply if the image is full-width', choices=[(b'right', b'right'), (b'left', b'left')])), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Caption')), (b'is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check to add a horizontal rule line to bottom of inset.', default=True, required=False, label=b'Has bottom rule line'))])), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'reusable_text', v1.blocks.ReusableTextChooserBlock(b'v1.ReusableText')), (b'email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'default_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', default=True, required=False, label=b'Default heading style')), (b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'inline_info', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Show disclaimer on same line as button. Only select this option if the disclaimer text is a few words (ie, "Privacy Act statement") rather than a full sentence.', required=False, label=b'Inline disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))]), required=False, icon=b'mail'))]))])), (b'expandable', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'extension', wagtail.wagtailcore.blocks.CharBlock(max_length=4, required=False)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A phoneword version of the above number', max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, label=b'TTY', required=False)), (b'tty_ext', wagtail.wagtailcore.blocks.CharBlock(max_length=4, label=b'TTY Extension', required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])), (b'expandable_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_accordion', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of expandable group.', default=False, required=False)), (b'expandables', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'extension', wagtail.wagtailcore.blocks.CharBlock(max_length=4, required=False)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A phoneword version of the above number', max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, label=b'TTY', required=False)), (b'tty_ext', wagtail.wagtailcore.blocks.CharBlock(max_length=4, label=b'TTY Extension', required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])))])), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'job_listing_table', wagtail.wagtailcore.blocks.StructBlock([(b'first_row_is_table_header', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the first row as a header.', default=True, required=False)), (b'first_col_is_header', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the first column as a header.', default=False, required=False)), (b'is_full_width', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the table at full width.', default=False, required=False)), (b'is_striped', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the table with striped rows.', default=False, required=False)), (b'is_stacked', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Stack the table columns on mobile.', default=True, required=False)), (b'empty_table_msg', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Message to display if there is no table data.', required=False, label=b'No Table Data Message')), (b'hide_closed', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Whether to hide jobs that are not currently open (jobs will automatically update)', default=True, required=False))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))])), (b'conference_registration_form', wagtail.wagtailcore.blocks.StructBlock([(b'govdelivery_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Conference registrants will be subscribed to this GovDelivery topic.', label='GovDelivery code')), (b'govdelivery_question_id', wagtail.wagtailcore.blocks.RegexBlock(help_text='Enter the ID of the question in GovDelivery that is being used to track registration for this conference. It is the number in the question URL, e.g., the <code>12345</code> in <code>https://admin.govdelivery.com/questions/12345/edit</code>.', regex='^\\d{5,}$', required=False, label='GovDelivery question ID', error_messages={'invalid': 'GovDelivery question ID must be 5 digits.'})), (b'govdelivery_answer_id', wagtail.wagtailcore.blocks.RegexBlock(help_text='Enter the ID of the affirmative answer for the above question. To find it, right-click on the answer in the listing on a page like <code>https://admin.govdelivery.com/questions/12345/answers</code>, inspect the element, and look around in the source for a five-digit ID associated with that answer. <strong>Required if Govdelivery question ID is set.</strong>', regex='^\\d{5,}$', required=False, label='GovDelivery answer ID', error_messages={'invalid': 'GovDelivery answer ID must be 5 digits.'})), (b'capacity', wagtail.wagtailcore.blocks.IntegerBlock(help_text='Enter the (physical) conference attendance limit as a number.')), (b'success_message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Enter a message that will be shown on successful registration.')), (b'at_capacity_message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Enter a message that will be shown when the event is at capacity.')), (b'failure_message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Enter a message that will be shown if the GovDelivery subscription fails.'))])), (b'raw_html_block', wagtail.wagtailcore.blocks.RawHTMLBlock(label=b'Raw HTML block')), (b'html_block', wagtail.wagtailcore.blocks.StructBlock([(b'html_url', wagtail.wagtailcore.blocks.RegexBlock(regex=b'^https://(s3.amazonaws.com/)?files.consumerfinance.gov/.+$', default=b'', required=True, error_messages={b'required': b'The HTML URL field is required for rendering raw HTML from a remote source.', b'invalid': b'The URL is invalid or not allowed. '}, label=b'Source URL'))])), (b'chart_block', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'chart_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'bar', b'Bar | % y-axis values'), (b'line', b'Line | millions/billions y-axis values'), (b'line-index', b'Line-Index | integer y-axis values'), (b'tile_map', b'Tile Map | grid-like USA map')])), (b'color_scheme', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Chart\'s color scheme. See "https://github.com/cfpb/cfpb-chart-builder#createchart-options-".', required=False, choices=[(b'blue', b'Blue'), (b'gold', b'Gold'), (b'green', b'Green'), (b'navy', b'Navy'), (b'neutral', b'Neutral'), (b'purple', b'Purple'), (b'teal', b'Teal')])), (b'data_source', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Location of the chart\'s data source relative to "https://files.consumerfinance.gov/data/". For example,"consumer-credit-trends/auto-loans/num_data_AUT.csv".', required=True)), (b'date_published', wagtail.wagtailcore.blocks.DateBlock(help_text=b'Automatically generated when CCT cron job runs')), (b'description', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Briefly summarize the chart for visually impaired users.', required=True)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of chart block.', default=False, required=False)), (b'last_updated_projected_data', wagtail.wagtailcore.blocks.DateBlock(help_text=b'Month of latest entry in dataset')), (b'metadata', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional metadata for the chart to use. For example, with CCT this would be the chart\'s "group".', required=False)), (b'note', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Text to display as a footnote. For example, "Data from the last six months are not final."', required=False)), (b'y_axis_label', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Custom y-axis label. NOTE: Line-Index chart y-axis is not overridable with this field!', required=False))])), (b'mortgage_chart_block', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'title', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', required=True)), (b'description', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Chart summary for visually impaired users.', required=False)), (b'note', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Text for "Note" section of footnotes.', required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of chart block.', default=False, required=False))])), (b'mortgage_map_block', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'title', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', required=True)), (b'description', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Chart summary for visually impaired users.', required=False)), (b'note', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Text for "Note" section of footnotes.', required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of chart block.', default=False, required=False))])), (b'mortgage_downloads_block', wagtail.wagtailcore.blocks.StructBlock([(b'show_archives', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Check this box to allow the archival section to display. No section will appear if there are no archival downloads.', default=False, required=False))])), (b'snippet_list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of snippet list.', default=False, required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'actions_column_width', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Choose the width in % that you wish to set the Actions column in a snippet list.', required=False, choices=[(b'70', b'70%'), (b'66', b'66%'), (b'60', b'60%'), (b'50', b'50%'), (b'40', b'40%'), (b'33', b'33%'), (b'30', b'30%')], label=b'Width of "Actions" column')), (b'snippet_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=v1.atomic_elements.organisms.get_snippet_type_choices)), (b'show_thumbnails', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"If selected, each snippet in the list will include a 150px-wide image from the snippet's thumbnail field.", required=False)), (b'actions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link_label', wagtail.wagtailcore.blocks.CharBlock(help_text=b'E.g., "Download" or "Order free prints"')), (b'snippet_field', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Corresponds to the available fields for the selected snippet type.', choices=v1.atomic_elements.organisms.get_snippet_field_choices))]))), (b'tags', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Tag'), help_text=b'Enter tag names to filter the snippets. For a snippet to match and be output in the list, it must have been tagged with all of the tag names listed here. The tag names are case-insensitive.'))])), (b'data_snapshot', wagtail.wagtailcore.blocks.StructBlock([(b'market_key', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Market identifier, e.g. AUT', max_length=20, required=True)), (b'num_originations', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Number of originations, e.g. 1.2 million', max_length=20)), (b'value_originations', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Total dollar value of originations, e.g. $3.4 billion', max_length=20)), (b'year_over_year_change', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Percentage change, e.g. 5.6% increase', max_length=20)), (b'last_updated_projected_data', wagtail.wagtailcore.blocks.DateBlock(help_text=b'Month of latest entry in dataset')), (b'num_originations_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Descriptive sentence, e.g. Auto loans originated', max_length=100)), (b'value_originations_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Descriptive sentence, e.g. Dollar volume of new loans', max_length=100)), (b'year_over_year_change_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Descriptive sentence, e.g. In year-over-year originations', max_length=100)), (b'inquiry_month', wagtail.wagtailcore.blocks.DateBlock(help_text=b'Month of latest entry in dataset for inquiry data', max_length=20, required=False)), (b'inquiry_year_over_year_change', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Percentage change, e.g. 5.6% increase', max_length=20, required=False)), (b'inquiry_year_over_year_change_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Descriptive sentence, e.g. In year-over-year inquiries', max_length=100, required=False)), (b'denial_month', wagtail.wagtailcore.blocks.DateBlock(help_text=b'Month of latest entry in dataset for denial data', max_length=20, required=False)), (b'denial_year_over_year_change', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Percentage change, e.g. 5.6% increase', max_length=20, required=False)), (b'denial_year_over_year_change_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Descriptive sentence, e.g. In year-over-year credit tightness', max_length=100, required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False, icon=b'image'))])), (b'image_text_25_75_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", default=False, required=False)), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])))])), (b'image_text_50_50_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", default=False, required=False)), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', required=False, label=b'Include sharing links?')), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))])), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'half_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'third_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))]))], blank=True),
        ),
    ]
