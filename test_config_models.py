import constants
import logging
import servicemanager
import testing_utils
import config_models
import hypertts


def test_voice_selection(qtbot):
    # test the models around voice selection
    # =======================================

    manager = servicemanager.ServiceManager(testing_utils.get_test_services_dir(), 'test_services')
    manager.init_services()
    manager.get_service('ServiceA').set_enabled(True)
    manager.get_service('ServiceB').set_enabled(True)
    voice_list = manager.full_voice_list()    

    anki_utils = testing_utils.MockAnkiUtils({})
    hypertts_instance = hypertts.HyperTTS(anki_utils, manager)

    voice_a_1 = [x for x in voice_list if x.name == 'voice_a_1'][0]
    voice_jane = [x for x in voice_list if x.name == 'jane'][0]

    # single voice mode
    # =================

    single = config_models.VoiceSelectionSingle()
    single.set_voice(config_models.VoiceWithOptions(voice_a_1, {'speed': 42}))

    expected_output = {
        'voice_selection_mode': 'single',
        'voice': {
            'voice': {
                'gender': 'Male', 
                'language': 'fr_FR', 
                'name': 'voice_a_1', 
                'service': 'ServiceA',
                'voice_key': {'name': 'voice_1'}
            },
            'options': {
                'speed': 42
            }
        }
    }
    assert single.serialize() == expected_output

    # test deserialization
    single_deserialized = hypertts_instance.deserialize_voice_selection(single.serialize())

    # check that it gives the same output
    assert single_deserialized.serialize() == expected_output


    # random voice mode
    # =================

    random = config_models.VoiceSelectionRandom()
    random.add_voice(config_models.VoiceWithOptionsRandom(voice_a_1, {'speed': 43}))
    random.add_voice(config_models.VoiceWithOptionsRandom(voice_jane, {}))

    expected_output = {
        'voice_selection_mode': 'random',
        'voice_list': [
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 43
                },
                'weight': 1
            },
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'ja_JP', 
                    'name': 'jane', 
                    'service': 'ServiceB',
                    'voice_key': {'voice_id': 'jane'}
                },
                'options': {
                },
                'weight': 1
            },            
        ]
    }
    assert random.serialize() == expected_output

    random.set_random_weight(1, 3)
    expected_output['voice_list'][1]['weight'] = 3

    assert random.serialize() == expected_output

    # test deserialization
    random_deserialized = hypertts_instance.deserialize_voice_selection(random.serialize())

    # check that it gives the same output
    assert random_deserialized.serialize() == expected_output


    random.remove_voice(1)
    del expected_output['voice_list'][1]

    assert random.serialize() == expected_output

    # priority voice mode
    # ===================

    priority = config_models.VoiceSelectionPriority()
    priority.add_voice(config_models.VoiceWithOptionsPriority(voice_a_1, {'speed': 43}))
    priority.add_voice(config_models.VoiceWithOptionsPriority(voice_a_1, {'speed': 84}))
    priority.add_voice(config_models.VoiceWithOptionsPriority(voice_jane, {}))

    expected_output = {
        'voice_selection_mode': 'priority',
        'voice_list': [
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 43
                },
            },
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 84
                },
            },            
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'ja_JP', 
                    'name': 'jane', 
                    'service': 'ServiceB',
                    'voice_key': {'voice_id': 'jane'}
                },
                'options': {
                },
            },            
        ]
    }
    assert priority.serialize() == expected_output

    priority.move_up_voice(2)

    expected_output = {
        'voice_selection_mode': 'priority',
        'voice_list': [
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 43
                },
            },
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'ja_JP', 
                    'name': 'jane', 
                    'service': 'ServiceB',
                    'voice_key': {'voice_id': 'jane'}
                },
                'options': {
                },
            },
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 84
                },
            },            
        ]
    }
    assert priority.serialize() == expected_output    


    priority.move_down_voice(0)

    expected_output = {
        'voice_selection_mode': 'priority',
        'voice_list': [
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'ja_JP', 
                    'name': 'jane', 
                    'service': 'ServiceB',
                    'voice_key': {'voice_id': 'jane'}
                },
                'options': {
                },
            },
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 43
                },
            },
            {
                'voice': {
                    'gender': 'Male', 
                    'language': 'fr_FR', 
                    'name': 'voice_a_1', 
                    'service': 'ServiceA',
                    'voice_key': {'name': 'voice_1'}
                },
                'options': {
                    'speed': 84
                },
            },            
        ]
    }
    assert priority.serialize() == expected_output

    # test deserialization
    priority_deserialized = hypertts_instance.deserialize_voice_selection(priority.serialize())

    # check that it gives the same output
    assert priority_deserialized.serialize() == expected_output