import sys
import logging
import aqt
import anki.utils
import re

if hasattr(sys, '_pytest_mode'):
    import constants
    import errors
else:
    from . import constants
    from . import errors


REGEXP_REALTIME_SIMPLE_TEMPLATE = '.*<hypertts-template\s+setting="(.*)"\s+version="(.*)">(.*)</hypertts-template>.*'
REGEXP_REALTIME_ADVANCED_TEMPLATE = '.*<hypertts-template-advanced\s+setting="(.*)"\s+version="(.*)">\n(.*)</hypertts-template-advanced>.*'

def extract_template_regexp(input, regexp):
    match_result = re.match(regexp, input, re.DOTALL)
    if match_result == None:
        return None
    setting = match_result.group(1).strip()
    version_str = match_result.group(2).strip()
    version = constants.TemplateFormatVersion[version_str]
    content = match_result.group(3).strip()
    return setting, version, content

def extract_simple_template(input):
    return extract_template_regexp(input, REGEXP_REALTIME_SIMPLE_TEMPLATE)

def extract_advanced_template(input):
    return extract_template_regexp(input, REGEXP_REALTIME_ADVANCED_TEMPLATE)


def process_text(source_text, text_processing_model):
    processed_text = anki.utils.htmlToTextLine(source_text)
    for text_replacement_rule in text_processing_model.text_replacement_rules:
        processed_text = process_text_replacement_rule(processed_text, text_replacement_rule)
    return processed_text

def process_text_replacement_rule(input_text, rule):
    try:
        if rule.rule_type == constants.TextReplacementRuleType.Regex:
            result = re.sub(rule.source, rule.target, input_text)
        elif rule.rule_type == constants.TextReplacementRuleType.Simple:
            result = input_text.replace(rule.source,  rule.target)
        else:
            raise Exception(f'unsupported replacement rule type: {rule.rule_type}')
        return result
    except Exception as e:
        raise errors.TextReplacementError(input_text, rule.source, rule.target, str(e))

