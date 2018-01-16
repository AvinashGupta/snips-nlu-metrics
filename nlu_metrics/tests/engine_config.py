from __future__ import unicode_literals

NLU_CONFIG = {
    "unit_name": "nlu_engine",
    "intent_parsers_configs": [
        {
            "unit_name": "deterministic_intent_parser",
            "max_queries": 50,
            "max_entities": 200
        },
        {
            "unit_name": "probabilistic_intent_parser",
            "intent_classifier_config": {
                "data_augmentation_config": {
                    "min_utterances": 20,
                    "unknown_words_replacement_string": None,
                    "noise_factor": 5,
                    "unknown_word_prob": 0
                },
                "unit_name": "log_reg_intent_classifier",
                "featurizer_config": {
                    "sublinear_tf": False
                },
                "random_seed": None,
                "log_reg_args": {
                    "penalty": "l2",
                    "loss": "log",
                    "n_iter": 5,
                    "n_jobs": -1,
                    "class_weight": "balanced"
                }
            },
            "slot_filler_config": {
                "data_augmentation_config": {
                    "capitalization_ratio": 0.2,
                    "min_utterances": 200
                },
                "unit_name": "crf_slot_filler",
                "entities_offsets": [
                    -2,
                    -1,
                    0
                ],
                "crf_args": {
                    "c2": 0.1,
                    "c1": 0.1,
                    "algorithm": "lbfgs"
                },
                "tagging_scheme": 1,
                "random_seed": None,
                "feature_factory_configs": [
                    {
                        "args": {
                            "common_words_gazetteer_name": None,
                            "use_stemming": True,
                            "n": 1
                        },
                        "factory_name": "ngram",
                        "offsets": [
                            -2,
                            -1,
                            0,
                            1,
                            2
                        ]
                    },
                    {
                        "args": {
                            "common_words_gazetteer_name": None,
                            "use_stemming": True,
                            "n": 2
                        },
                        "factory_name": "ngram",
                        "offsets": [
                            -2,
                            1
                        ]
                    },
                    {
                        "args": {},
                        "factory_name": "is_digit",
                        "offsets": [
                            -1,
                            0,
                            1
                        ]
                    },
                    {
                        "args": {},
                        "factory_name": "is_first",
                        "offsets": [
                            -2,
                            -1,
                            0
                        ]
                    },
                    {
                        "args": {},
                        "factory_name": "is_last",
                        "offsets": [
                            0,
                            1,
                            2
                        ]
                    },
                    {
                        "args": {
                            "n": 1
                        },
                        "factory_name": "shape_ngram",
                        "offsets": [
                            0
                        ]
                    },
                    {
                        "args": {
                            "n": 2
                        },
                        "factory_name": "shape_ngram",
                        "offsets": [
                            -1,
                            0
                        ]
                    },
                    {
                        "args": {
                            "n": 3
                        },
                        "factory_name": "shape_ngram",
                        "offsets": [
                            -1
                        ]
                    },
                    {
                        "args": {
                            "tagging_scheme_code": 2,
                            "use_stemming": True
                        },
                        "factory_name": "entity_match",
                        "drop_out": 0.1,
                        "offsets": [
                            -2,
                            -1,
                            0
                        ]
                    },
                    {
                        "args": {
                            "tagging_scheme_code": 1
                        },
                        "factory_name": "builtin_entity_match",
                        "offsets": [
                            -2,
                            -1,
                            0
                        ]
                    }
                ],
                "exhaustive_permutations_threshold": 64
            }
        }
    ]
}
