#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create CMS Simulated Dataset records.
"""

import glob
import json
import re
import subprocess
import sys

from create_das_json_store import get_das_json, get_from_deep_json
from create_config_download_script import get_input_dataset

LINK_INFO = {}
exec(open('./outputs/config_files_link_info.py', 'r').read())

LINK_INFO = {
  '7daa6d84dd09f0024e982d7b91430774': 3000,
  'a8b87e4a93ad780670c2864baf05a71f': 3001,
  '4515630011652d2fbae85c3707cb6ffb': 3002,
  '7e87e26a3ecea5744a10820db28e87bf': 3003,
  '7daa6d84dd09f0024e982d7b916a69a2': 3004,
  '0d0714743f0204ed3c0144941e6ce248': 3005,
  '30e13855854aafbbf5042c9d7f51aba8': 3006,
  '7e87e26a3ecea5744a10820db28f4f49': 3007,
  '98e64546356a58b305c61f910174222c': 3008,
  '7daa6d84dd09f0024e982d7b91638ee9': 3009,
  '0d0714743f0204ed3c0144941e703c2e': 3010,
  '0d0714743f0204ed3c0144941e6c7389': 3011,
  'c637c5fe20bd26655249c48bc95bbd6e': 3012,
  'c637c5fe20bd26655249c48bc942efba': 3013,
  '7c7c0e8e128b3d1a9f287090342346e0': 3014,
  'c5215c4f10370f5925caa5695cd8d1a0': 3015,
  '4a1f22052abb5b3c51ee42f4dcdee483': 3016,
  'a8b87e4a93ad780670c2864baf082009': 3017,
  '7daa6d84dd09f0024e982d7b916a2a58': 3018,
  'c5215c4f10370f5925caa5695ce3da3f': 3019,
  'a8b87e4a93ad780670c2864baf0e401e': 3020,
  '0d0714743f0204ed3c0144941e6c4391': 3021,
  'e75da0ef8a4c51a102040e9de55910b1': 3022,
  'a8b87e4a93ad780670c2864baf0d425d': 3023,
  '0d0714743f0204ed3c0144941e6c3430': 3024,
  '0d0714743f0204ed3c0144941e6c544b': 3025,
  '30e13855854aafbbf5042c9d7f4f38c2': 3026,
  'a3e9a49adb11d7079eda533cfa26a199': 3027,
  '532578856e4aba9f49cb063f9baed097': 3028,
  '82684178352d5f0db3b347b48c60ffe7': 3029,
  'c8c18849c66ed34bafa1f8cb42279272': 3030,
  'b25309c97c5b8870f77c36c91bb9bb48': 3031,
  'f39b8d56dd05ca1999a63e01752419fa': 3032,
  '7daa6d84dd09f0024e982d7b914912ac': 3033,
  'c5215c4f10370f5925caa5695cc9663d': 3034,
  '7daa6d84dd09f0024e982d7b914557cf': 3035,
  'c637c5fe20bd26655249c48bc9384974': 3036,
  'b78f836a8fc0457f3d1cf47679205dce': 3037,
  'cbb3e0ee51f19be8f8a04cf25963e402': 3038,
  '7b0f1f8e4df3d63108f095f9fa57f554': 3039,
  '98e64546356a58b305c61f91017475f2': 3040,
  '7daa6d84dd09f0024e982d7b9143d801': 3041,
  '0cac1a565bda09ad57a6810efe437c3a': 3042,
  '0d0714743f0204ed3c0144941e6d0236': 3043,
  'e22b2bb5b0981d6ba66a06f53eec1a6e': 3044,
  'f39b8d56dd05ca1999a63e017523ff89': 3045,
  '6c6ff3f35efb680aebe72ced3d0211de': 3046,
  'a8b87e4a93ad780670c2864baf2c69c1': 3047,
  '947fc12e45a0789d78f4cf2e4a6c4978': 3048,
  '8d6b90fd328fcdf734c4595f7086f4aa': 3049,
  '947fc12e45a0789d78f4cf2e4a6cc7f4': 3050,
  '98e64546356a58b305c61f9101748d9e': 3051,
  '7daa6d84dd09f0024e982d7b91457b5a': 3052,
  '947fc12e45a0789d78f4cf2e4a6ce5eb': 3053,
  '9e0fb63675bdd7dc5283db9af45df5c2': 3054,
  'e75da0ef8a4c51a102040e9de556aa6a': 3055,
  '0d0714743f0204ed3c0144941e7205ac': 3056,
  '4a1f22052abb5b3c51ee42f4dcdf63a5': 3057,
  '98e64546356a58b305c61f91017460b2': 3058,
  '2e0a80c07f23808d4b75c974eaf58837': 3059,
  '7daa6d84dd09f0024e982d7b916a3d21': 3060,
  '0d0714743f0204ed3c0144941e6b5c4e': 3061,
  '30e13855854aafbbf5042c9d7f520eec': 3062,
  '7bb91b34c2fcdd08f00eb3d3191f5cf4': 3063,
  'f39b8d56dd05ca1999a63e017523fa17': 3064,
  'caf0a1e27e00a4ac2cf66edbe3650da8': 3065,
  '8d6b90fd328fcdf734c4595f708e40a7': 3066,
  '98e64546356a58b305c61f9101741485': 3067,
  '7daa6d84dd09f0024e982d7b915008a0': 3068,
  '4515630011652d2fbae85c3707cb762c': 3069,
  'a8b87e4a93ad780670c2864baf01b27e': 3070,
  '47de7af4e28799c29752ba690346afb7': 3071,
  '0d0714743f0204ed3c0144941e91b14d': 3072,
  'c9e000c71f90818cafc2ea88b2e7e184': 3073,
  '6602d94fea27826ae6e8e0fcd3cb1667': 3074,
  'a8b87e4a93ad780670c2864baf3961dd': 3075,
  '8c6e215a3026002258a2dbea0b28203e': 3076,
  '947fc12e45a0789d78f4cf2e4a6cd449': 3077,
  '0d0714743f0204ed3c0144941e6c4942': 3078,
  '9181dcfde0729882b44992132015be09': 3079,
  '98e64546356a58b305c61f9101743bed': 3080,
  '7bb91b34c2fcdd08f00eb3d3191ef9d6': 3081,
  '1156e999350f625b865f0777d7f9b7df': 3082,
  'e75da0ef8a4c51a102040e9de55404a1': 3083,
  '23c01d3a9a0824b0bc16413a3cb886a3': 3084,
  '0cac1a565bda09ad57a6810efe44961c': 3085,
  '2f1e2ccb71a5dc3b16aeb4bc3e72fdb1': 3086,
  'e22b2bb5b0981d6ba66a06f53ec457e6': 3087,
  '9ebe5de2113c461586671dca1e09299d': 3088,
  'c5215c4f10370f5925caa5695cd5176f': 3089,
  '7daa6d84dd09f0024e982d7b916a093c': 3090,
  'c637c5fe20bd26655249c48bc95bd0a9': 3091,
  'e75da0ef8a4c51a102040e9de555c9b3': 3092,
  'c5215c4f10370f5925caa5695cdafbdd': 3093,
  '7bb91b34c2fcdd08f00eb3d3191f0786': 3094,
  '7e87e26a3ecea5744a10820db2908f57': 3095,
  '7daa6d84dd09f0024e982d7b91639ba5': 3096,
  '23c01d3a9a0824b0bc16413a3cb8a7af': 3097,
  '4f1f909dc818ac109c868566853a100b': 3098,
  'c637c5fe20bd26655249c48bc9456bf3': 3099,
  '6d737d082061a17da3b72f6b365e646c': 3100,
  'eee98ac39b28e880d1fcff7934dc2071': 3101,
  'c5215c4f10370f5925caa5695cd575d6': 3102,
  'c5215c4f10370f5925caa5695cdb4a55': 3103,
  '9e0fb63675bdd7dc5283db9af45da3f9': 3104,
  '0d0714743f0204ed3c0144941e6b5026': 3105,
  'c637c5fe20bd26655249c48bc95bc89c': 3106,
  '1156e999350f625b865f0777d7f89e82': 3107,
  '787d59798ba1957342f08d4d11fd40d1': 3108,
  '5a969e363f8f7c70403095bd1ed4059a': 3109,
  '6d737d082061a17da3b72f6b36620512': 3110,
  'c9e000c71f90818cafc2ea88b2e7e2b7': 3111,
  'e22b2bb5b0981d6ba66a06f53eea9c7b': 3112,
  '7daa6d84dd09f0024e982d7b914fc3e6': 3113,
  '7daa6d84dd09f0024e982d7b914fe535': 3114,
  '947fc12e45a0789d78f4cf2e4a6ccb70': 3115,
  'c729fce63ed969fa8b51acab368c394e': 3116,
  'a8b87e4a93ad780670c2864baf0149b4': 3117,
  '40f18a4101a71b9631b737ae01700e35': 3118,
  'b17ed01fdcb093aaf395ab27ff34e3bd': 3119,
  '6c6ff3f35efb680aebe72ced3d024dc2': 3120,
  '23c01d3a9a0824b0bc16413a3cb8bd98': 3121,
  '98e64546356a58b305c61f9101742e06': 3122,
  '8d6b90fd328fcdf734c4595f7091cd60': 3123,
  '0d0714743f0204ed3c0144941e7089e4': 3124,
  '51bf5a6e98020fb8fa6dece923ed59d1': 3125,
  '0d0714743f0204ed3c0144941e708382': 3126,
  '983b066ccca9897c4131e0559ae28aa4': 3127,
  '532578856e4aba9f49cb063f9baec169': 3128,
  '23c01d3a9a0824b0bc16413a3cb89677': 3129,
  '0de33f0c9cb94c9f73cd4e86d85bc166': 3130,
  'fa79ed2f93428d49ddb4d27246d78312': 3131,
  '29be6bf0a7154bef099908f61c134f32': 3132,
  'e22b2bb5b0981d6ba66a06f53ebc76de': 3133,
  'b78f836a8fc0457f3d1cf4767948a508': 3134,
  '947fc12e45a0789d78f4cf2e4a6dfc47': 3135,
  '6c6ff3f35efb680aebe72ced3d010e42': 3136,
  '7bb91b34c2fcdd08f00eb3d3191f8a11': 3137,
  '4866695a076ae48d093c752532bd8bff': 3138,
  '7e87e26a3ecea5744a10820db28f6a0b': 3139,
  '664dd7856adaa0b955b09f1433e374c4': 3140,
  'c5215c4f10370f5925caa5695cd75400': 3141,
  '0d0714743f0204ed3c0144941e6b61a1': 3142,
  '7daa6d84dd09f0024e982d7b9142fcdd': 3143,
  '47de7af4e28799c29752ba69033f98ec': 3144,
  'c637c5fe20bd26655249c48bc93d44ba': 3145,
  '796833acecbdb5e17bde7cd309059294': 3146,
  '23c01d3a9a0824b0bc16413a3cb8ae2b': 3147,
  '30e13855854aafbbf5042c9d7f521a2e': 3148,
  'c5215c4f10370f5925caa5695cd570f4': 3149,
  'e75da0ef8a4c51a102040e9de558d69d': 3150,
  '23c01d3a9a0824b0bc16413a3cb8a909': 3151,
  '2e0a80c07f23808d4b75c974eaf56214': 3152,
  '98e64546356a58b305c61f91017424d9': 3153,
  '7daa6d84dd09f0024e982d7b916a0ec2': 3154,
  'c5215c4f10370f5925caa5695cda3a44': 3155,
  'c637c5fe20bd26655249c48bc942b5c9': 3156,
  '4515630011652d2fbae85c3707cb6303': 3157,
  'c637c5fe20bd26655249c48bc95e0251': 3158,
  'e22b2bb5b0981d6ba66a06f53e0089cb': 3159,
  '532578856e4aba9f49cb063f9baec55b': 3160,
  '8d6b90fd328fcdf734c4595f70e2c87c': 3161,
  '88d21e388acd9191c9e326ff6dc48d10': 3162,
  '7daa6d84dd09f0024e982d7b9163813d': 3163,
  'a8b87e4a93ad780670c2864baf097785': 3164,
  '7daa6d84dd09f0024e982d7b916a7718': 3165,
  'a8b87e4a93ad780670c2864baf01bf87': 3166,
  '584825b69f5a095993efd0af12bb5e42': 3167,
  '51bf5a6e98020fb8fa6dece923ed48d8': 3168,
  '7b0f1f8e4df3d63108f095f9fa57f7ab': 3169,
  '9e0fb63675bdd7dc5283db9af45dee2f': 3170,
  '0d0714743f0204ed3c0144941e6ce0aa': 3171,
  '0d0714743f0204ed3c0144941e8df5e4': 3172,
  'e22b2bb5b0981d6ba66a06f53ebd51c7': 3173,
  'c637c5fe20bd26655249c48bc91b8a2d': 3174,
  'f23324c0cc10d31c5a86d5e5ecc18194': 3175,
  '5889fd7a33a3028626be5391385a468f': 3176,
  'fc458394c2843a2ab77397966d51b3c0': 3177,
  '222fee3fd4cf6edf83c4f37ad062d132': 3178,
  'a8b87e4a93ad780670c2864baf081293': 3179,
  'a8b87e4a93ad780670c2864baf370842': 3180,
  '2f1e2ccb71a5dc3b16aeb4bc3e7300cc': 3181,
  'c5215c4f10370f5925caa5695ccc7bf7': 3182,
  '1f48c8f34162458caedc7b1af94a232c': 3183,
  '88d21e388acd9191c9e326ff6dc478a3': 3184,
  '0d0714743f0204ed3c0144941e703972': 3185,
  '0d0714743f0204ed3c0144941e6ce548': 3186,
  'c5215c4f10370f5925caa5695cdca324': 3187,
  '88d21e388acd9191c9e326ff6dcafcff': 3188,
  'e057b5071cdc2df588be80e24a131404': 3189,
  'a8b87e4a93ad780670c2864baf3cf54d': 3190,
  'b17ed01fdcb093aaf395ab27ff353404': 3191,
  '4a1f22052abb5b3c51ee42f4dcdf5de7': 3192,
  'd7c7e40a2583db7d5ecc08b5c9b12d26': 3193,
  'c5215c4f10370f5925caa5695cd7a448': 3194,
  '0d0714743f0204ed3c0144941e6b407b': 3195,
  '584825b69f5a095993efd0af12bb32cd': 3196,
  '9181dcfde0729882b449921320147b6e': 3197,
  '04afaf020d06de306b97edf3a0461d24': 3198,
  'a8b87e4a93ad780670c2864baf024c8a': 3199,
  '339cd62364712af8a4d594691b415ac1': 3200,
  '0d0714743f0204ed3c0144941e8ea2cd': 3201,
  '7e87e26a3ecea5744a10820db2931b0d': 3202,
  '5d08a4b52573d04c228c9be58e7ba7ed': 3203,
  '1f48c8f34162458caedc7b1af94a180a': 3204,
  'a8b87e4a93ad780670c2864baf09dde3': 3205,
  '7e87e26a3ecea5744a10820db28f7d3f': 3206,
  '7daa6d84dd09f0024e982d7b9163680d': 3207,
  '76dd68e16f83f9e75ac62a241e2ff844': 3208,
  'a8b87e4a93ad780670c2864baf01ca14': 3209,
  '3aca8f1bdff067de8609ce4479b9fffc': 3210,
  'c5215c4f10370f5925caa5695cdb60c7': 3211,
  '7bb91b34c2fcdd08f00eb3d3191f6796': 3212,
  'e22b2bb5b0981d6ba66a06f53ebefdcb': 3213,
  '5d08a4b52573d04c228c9be58e7c9ab8': 3214,
  'c637c5fe20bd26655249c48bc94e8056': 3215,
  '23c01d3a9a0824b0bc16413a3cb8c7ef': 3216,
  'a8b87e4a93ad780670c2864baf09a4d8': 3217,
  '6c6ff3f35efb680aebe72ced3d012006': 3218,
  '7c7c0e8e128b3d1a9f287090342312e2': 3219,
  'e22b2bb5b0981d6ba66a06f53ec793ac': 3220,
  'c9e000c71f90818cafc2ea88b2e7f02c': 3221,
  '947fc12e45a0789d78f4cf2e4a6cfb7b': 3222,
  '7daa6d84dd09f0024e982d7b91455828': 3223,
  '947fc12e45a0789d78f4cf2e4a6d0393': 3224,
  '7e87e26a3ecea5744a10820db2951c61': 3225,
  'cbb3e0ee51f19be8f8a04cf25963e11a': 3226,
  'a8b87e4a93ad780670c2864baf371d91': 3227,
  '7daa6d84dd09f0024e982d7b9143d1cf': 3228,
  'c08df1fda127154276e899c872a73726': 3229,
  'bba69ae19e1fbc577b22ff7379801965': 3230,
  '7bb91b34c2fcdd08f00eb3d3191f4e0a': 3231,
  '6c6ff3f35efb680aebe72ced3d0114b3': 3232,
  '30e13855854aafbbf5042c9d7f4f344f': 3233,
  'a8b87e4a93ad780670c2864baf3692b1': 3234,
  'c5215c4f10370f5925caa5695cd7ae8d': 3235,
  'c637c5fe20bd26655249c48bc94e7575': 3236,
  'c9e000c71f90818cafc2ea88b2e92143': 3237,
  '7e87e26a3ecea5744a10820db28f5b74': 3238,
  'e75da0ef8a4c51a102040e9de559091e': 3239,
  '0de33f0c9cb94c9f73cd4e86d85bb408': 3240,
  'c637c5fe20bd26655249c48bc95ea473': 3241,
  '222fee3fd4cf6edf83c4f37ad06aee2e': 3242,
  'f39b8d56dd05ca1999a63e017522b2bd': 3243,
  '0d0714743f0204ed3c0144941e701da7': 3244,
  'b78f836a8fc0457f3d1cf476794b8075': 3245,
  '47de7af4e28799c29752ba69033fa308': 3246,
  '947fc12e45a0789d78f4cf2e4a6c4761': 3247,
  '222fee3fd4cf6edf83c4f37ad06ace96': 3248,
  '9ebe5de2113c461586671dca1e0933a5': 3249,
  '787d59798ba1957342f08d4d11fd908b': 3250,
  'c5215c4f10370f5925caa5695cda44c5': 3251,
  'e22b2bb5b0981d6ba66a06f53ec02a75': 3252,
  'f0d6b2bf7129ab2b0e2d083668b685d9': 3253,
  'a8b87e4a93ad780670c2864baf010f0e': 3254,
  '510c7148bdece85b1d05dd872b265ad9': 3255,
  '6d737d082061a17da3b72f6b365fdf38': 3256,
  '7e87e26a3ecea5744a10820db28f6d80': 3257,
  'd4a9628510529dee2af9af0bc92340b8': 3258,
  '7daa6d84dd09f0024e982d7b914fc5e9': 3259,
  'a8b87e4a93ad780670c2864baf378daa': 3260,
  '0d0714743f0204ed3c0144941e71ebbc': 3261,
  'a8b87e4a93ad780670c2864baf02765b': 3262,
  '47de7af4e28799c29752ba69033e3a47': 3263,
  '8d6b90fd328fcdf734c4595f70e92ced': 3264,
  '7c7c0e8e128b3d1a9f28709034230d8c': 3265,
  'bae16f62ba4e90393266e2b342d1d10a': 3266,
  '7bb91b34c2fcdd08f00eb3d3191f5c81': 3267,
  '98e64546356a58b305c61f9101741df0': 3268,
  '7daa6d84dd09f0024e982d7b9144bb8e': 3269,
  'c5215c4f10370f5925caa5695cd7ae5f': 3270,
  'c5215c4f10370f5925caa5695cceb077': 3271,
  'a8b87e4a93ad780670c2864baf017225': 3272,
  'd1e71d39919455bc55d126c5a80192dd': 3273,
  'a3e9a49adb11d7079eda533cfa1f8b39': 3274,
  'e22b2bb5b0981d6ba66a06f53e006ee3': 3275,
  '88d21e388acd9191c9e326ff6dc48a67': 3276,
  '7bb91b34c2fcdd08f00eb3d3191f57e2': 3277,
  '7daa6d84dd09f0024e982d7b916a55aa': 3278,
  'a8b87e4a93ad780670c2864baf00f661': 3279,
  '62bbbeb9072f4819cb9a6a0673240e80': 3280,
  '23c01d3a9a0824b0bc16413a3cb8b900': 3281,
  '2e0a80c07f23808d4b75c974eaf57bbc': 3282,
  'a18d736b69d54ffbc617374d326dd3fd': 3283,
  '222fee3fd4cf6edf83c4f37ad06b200b': 3284,
  '7bb91b34c2fcdd08f00eb3d3191f1560': 3285,
  '45f0d743eb37f734b1c0870479dd06d4': 3286,
  'a8b87e4a93ad780670c2864baf023d61': 3287,
  '947fc12e45a0789d78f4cf2e4a6c3c6d': 3288,
  'a8b87e4a93ad780670c2864baf369d8a': 3289,
  '76dd68e16f83f9e75ac62a241e303b48': 3290,
  'a8b87e4a93ad780670c2864baf023e33': 3291,
  '947fc12e45a0789d78f4cf2e4a6d091f': 3292,
  'd7c7e40a2583db7d5ecc08b5c9b12a62': 3293,
  'e75da0ef8a4c51a102040e9de559dfbe': 3294,
  '41e90e49470d54645977450d28d23740': 3295,
  '947fc12e45a0789d78f4cf2e4a6d0bcd': 3296,
  '98e64546356a58b305c61f9101745520': 3297,
  '30e13855854aafbbf5042c9d7f51f811': 3298,
  'a8b87e4a93ad780670c2864baf01ef7b': 3299,
  'a8b87e4a93ad780670c2864baf026adc': 3300,
  '9ebe5de2113c461586671dca1e091d6b': 3301,
  'a8b87e4a93ad780670c2864baf013da9': 3302,
  'd4a9628510529dee2af9af0bc92626b6': 3303,
  '6d737d082061a17da3b72f6b365e5591': 3304,
  '47de7af4e28799c29752ba690346aaf5': 3305,
  '40f18a4101a71b9631b737ae01701b7a': 3306,
  'e22b2bb5b0981d6ba66a06f53ec04500': 3307,
  '98e64546356a58b305c61f9101744b84': 3308,
  '7daa6d84dd09f0024e982d7b9144e254': 3309,
  'a97027acd9102d625e32a3b4f78e7a14': 3310,
  'f39b8d56dd05ca1999a63e017522bc72': 3311,
  '98e64546356a58b305c61f910173f2f5': 3312,
  'a3e9a49adb11d7079eda533cfa1f9ee3': 3313,
  'caf0a1e27e00a4ac2cf66edbe3651f28': 3314,
  'cbb3e0ee51f19be8f8a04cf2596463d2': 3315,
  '35f991cb1c1e772c0acaa98f4c796a89': 3316,
  '796833acecbdb5e17bde7cd309059dc6': 3317,
  'a8b87e4a93ad780670c2864baf3cf4ac': 3318,
  'a8b87e4a93ad780670c2864baf2cf92b': 3319,
  '7daa6d84dd09f0024e982d7b916a5f6b': 3320,
  '7daa6d84dd09f0024e982d7b91500162': 3321,
  'c5215c4f10370f5925caa5695cd507b4': 3322,
  '98e64546356a58b305c61f9101746b88': 3323,
  '6d737d082061a17da3b72f6b365ee6ab': 3324,
  '7e87e26a3ecea5744a10820db2932a7d': 3325,
  'c637c5fe20bd26655249c48bc9289a21': 3326,
  '0d0714743f0204ed3c0144941e6b7105': 3327,
  'e75da0ef8a4c51a102040e9de567d3b6': 3328,
  '76dd68e16f83f9e75ac62a241e301035': 3329,
  'a8b87e4a93ad780670c2864baf39cbbe': 3330,
  '4866695a076ae48d093c752532bd8133': 3331,
  'bd00ebc013d37b71001c73501add57a1': 3332,
  'c5215c4f10370f5925caa5695cd7295f': 3333,
  'a18d736b69d54ffbc617374d326decc3': 3334,
  '0d0714743f0204ed3c0144941e70bbef': 3335,
  '0de33f0c9cb94c9f73cd4e86d8560a62': 3336,
  '7bb91b34c2fcdd08f00eb3d3191f1c3a': 3337,
  '0de33f0c9cb94c9f73cd4e86d85b9364': 3338,
  '6602d94fea27826ae6e8e0fcd3ca7156': 3339,
  'a8b87e4a93ad780670c2864baf01d739': 3340,
  '62bbbeb9072f4819cb9a6a067323e45d': 3341,
  'e9503a7214b07c7c615203890ad7407d': 3342,
  '0d0714743f0204ed3c0144941e6c984f': 3343,
  '98e64546356a58b305c61f9101744922': 3344,
  '01a9d2b5582107b1dbc8e080145c42b4': 3345,
  '98e64546356a58b305c61f9101746efa': 3346,
  '947fc12e45a0789d78f4cf2e4a6cf399': 3347,
  '7bb91b34c2fcdd08f00eb3d3191f7f84': 3348,
  '88d21e388acd9191c9e326ff6dc45c17': 3349,
  'd7c7e40a2583db7d5ecc08b5c9b04488': 3350,
  '7e87e26a3ecea5744a10820db2952010': 3351,
  '3b550de389a8797af7b60cb845542d62': 3352,
  '98e64546356a58b305c61f9101740763': 3353,
  'f0d6b2bf7129ab2b0e2d083668b67ca0': 3354,
  '7e87e26a3ecea5744a10820db293246a': 3355,
  'f39b8d56dd05ca1999a63e0175229881': 3356,
  'e9503a7214b07c7c615203890adecf09': 3357,
  'a8b87e4a93ad780670c2864baf024355': 3358,
  '62bbbeb9072f4819cb9a6a067323f1ba': 3359,
  'cbb3e0ee51f19be8f8a04cf25964189c': 3360,
  '8d6b90fd328fcdf734c4595f70da3faf': 3361,
  'e75da0ef8a4c51a102040e9de555da99': 3362,
  'e22b2bb5b0981d6ba66a06f53ebcc0db': 3363,
  'a8b87e4a93ad780670c2864baf01534f': 3364,
  '23c01d3a9a0824b0bc16413a3cb89c0b': 3365,
  '47de7af4e28799c29752ba6903468f82': 3366,
  'c5215c4f10370f5925caa5695ccc51b5': 3367,
  '7daa6d84dd09f0024e982d7b9150006a': 3368,
  'a3e9a49adb11d7079eda533cfa1f8236': 3369,
  '0de33f0c9cb94c9f73cd4e86d85bc34e': 3370,
  'e057b5071cdc2df588be80e24a11fb92': 3371,
  '947fc12e45a0789d78f4cf2e4a6cf6f4': 3372,
  'a8b87e4a93ad780670c2864baf0a2a9b': 3373,
  '4866695a076ae48d093c752532bd83d4': 3374,
  'c9e000c71f90818cafc2ea88b2e7dc6e': 3375,
  'e75da0ef8a4c51a102040e9de553ce09': 3376,
  '7daa6d84dd09f0024e982d7b916352f3': 3377,
  '7daa6d84dd09f0024e982d7b9142efe4': 3378,
  '23c01d3a9a0824b0bc16413a3cb8c957': 3379,
  '0d0714743f0204ed3c0144941e702e3f': 3380,
  '0d0714743f0204ed3c0144941e6bdbeb': 3381,
  'c729fce63ed969fa8b51acab368c66c5': 3382,
  'c637c5fe20bd26655249c48bc92f24fc': 3383,
  '7c7c0e8e128b3d1a9f28709034231c06': 3384,
  'd7c7e40a2583db7d5ecc08b5c9b12c79': 3385,
  '30e13855854aafbbf5042c9d7f520829': 3386,
  '6d737d082061a17da3b72f6b36619685': 3387,
  'd7c7e40a2583db7d5ecc08b5c9b03da0': 3388,
  '47de7af4e28799c29752ba69033fb1f0': 3389,
  '9ee7ac18c8fac8c1a71e3a640bffcea0': 3390,
  '98e64546356a58b305c61f910174234f': 3391,
  '62bbbeb9072f4819cb9a6a067323c437': 3392,
  'e22b2bb5b0981d6ba66a06f53ec3b2e7': 3393,
  '62bbbeb9072f4819cb9a6a0673241858': 3394,
  '4a1f22052abb5b3c51ee42f4dcde9c69': 3395,
  'a8b87e4a93ad780670c2864baf01a589': 3396,
  '0d0714743f0204ed3c0144941e91811a': 3397,
  '6d737d082061a17da3b72f6b3660cc77': 3398,
  'e75da0ef8a4c51a102040e9de5556901': 3399,
  '7daa6d84dd09f0024e982d7b91695301': 3400,
  '62bbbeb9072f4819cb9a6a067324280c': 3401,
  'c5215c4f10370f5925caa5695cd9eb0e': 3402,
  'a3e9a49adb11d7079eda533cfa1ee549': 3403,
  '1156e999350f625b865f0777d7f9562d': 3404,
  'a8b87e4a93ad780670c2864baf018ce5': 3405,
  '7bb91b34c2fcdd08f00eb3d3191f06e4': 3406,
  '664dd7856adaa0b955b09f1433e38123': 3407,
  'c9e000c71f90818cafc2ea88b2e7da63': 3408,
  '7daa6d84dd09f0024e982d7b914461c7': 3409,
  'a97027acd9102d625e32a3b4f78c79ac': 3410,
  'a8b87e4a93ad780670c2864baf00ffcf': 3411,
}

RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="024" ind1="7" ind2=" ">
        <subfield code="2">DOI</subfield>
        <subfield code="a">%(doi)s</subfield>
    </datafield>
    <datafield tag="110" ind1=" " ind2=" ">
        <subfield code="a">CMS collaboration</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">%(title)s</subfield>
    </datafield>
    <datafield tag="246" ind1=" " ind2=" ">
        <subfield code="a">%(title_heading)s</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
        <subfield code="a">Dataset</subfield>
        <subfield code="e">%(nb_events)s</subfield>
        <subfield code="t">events</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
        <subfield code="f">%(nb_files)s</subfield>
        <subfield code="t">files</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
        <subfield code="b">%(nb_bytes)s</subfield>
        <subfield code="t">bytes in total</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
        <subfield code="b">CERN Open Data Portal</subfield>
        <subfield code="c">2016</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
        <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
        <subfield code="a"><![CDATA[
          <p>%(title_heading)s</p>
          <p>See the description of the simulated dataset names in: <a href="/about/CMS-Simulated-Dataset-Names">About CMS simulated dataset names</a>.</p>]]>
        </subfield>
    </datafield>
    <datafield tag="538" ind1=" " ind2=" ">
        <subfield code="a">Recommended release for analysis: CMSSW_5_3_32</subfield>
        <subfield code="b">Global tag: %(global_tag)s</subfield>
    </datafield>
    <datafield tag="540" ind1=" " ind2=" ">
        <subfield code="a">CC0</subfield>
    </datafield>
    <datafield tag="556" ind1=" " ind2=" ">
        <subfield code="a">These simulated datasets correspond to the collision data collected by the CMS experiment in 2011.</subfield>
    </datafield>
    <datafield tag="567" ind1=" " ind2=" ">
        <subfield code="a">%(generator_parameters)s</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
        <subfield code="a">You can access these data through the CMS Virtual Machine. See the instructions for setting up the Virtual Machine and getting started in</subfield>
        <subfield code="u">http://opendata.cern.ch/VM/CMS#2011</subfield>
        <subfield code="y">How to install the CMS Virtual Machine</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
        <subfield code="u">http://opendata.cern.ch/getting-started/CMS#2011</subfield>
        <subfield code="y">Getting started with CMS open data</subfield>
    </datafield>
    <datafield tag="583" ind1=" " ind2=" ">
        <subfield code="a">The generation and simulation of simulated Monte Carlo data has been validated through general CMS validation procedures.</subfield>
    </datafield>
    <datafield tag="593" ind1=" " ind2=" ">
        <subfield code="a">Generators: %(generators)s</subfield>
        <subfield code="b">Global tag: %(global_tag)s</subfield>
    </datafield>
    <datafield tag="655" ind1=" " ind2="7">
        <subfield code="a">%(category)s</subfield>
        <subfield code="9">CMS Collaboration</subfield>
    </datafield>
    <datafield tag="693" ind1=" " ind2=" ">
        <subfield code="a">CERN-LHC</subfield>
        <subfield code="e">CMS</subfield>
    </datafield>
    <datafield tag="770" ind1=" " ind2=" ">
        <subfield code="a">/MinBias_TuneZ2_7TeV-pythia6/Summer11Leg-START53_LV4-v1/GEN-SIM</subfield>
        <subfield code="w">3600</subfield>
    </datafield>
    <datafield tag="772" ind1=" " ind2=" ">
        <subfield code="a">%(raw)s</subfield>
    </datafield>
%(8567s)s
    <datafield tag="942" ind1=" " ind2=" ">
        <subfield code="e">7TeV</subfield>
    </datafield>
    <datafield tag="964" ind1=" " ind2="0">
        <subfield code="c">Run2011A</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
        <subfield code="a">CMS-Simulated-Datasets</subfield>
    </datafield>
%(FFTs)s
  </record>"""

TEMPLATE_FFT = """\
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-eos-file-indexes/%(filename)s</subfield>
      <subfield code="z">%(dataset)s dataset file index (%(nb_dataset)s of %(nb_total)s) for access to data via CMS virtual machine</subfield>
    </datafield>
"""

def create_8567s(dataset):
    out = ''
    junk, dataset_prefix, dataset_middle, dataset_suffix = dataset.split('/')
    dataset_version = dataset_middle[dataset_middle.index('PU_S13'):]
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*_%s_*xml' % (dataset_prefix, dataset_version))
    filenames.sort()
    for filename in filenames:
        out += open(filename, 'r').read()
        out = out.rstrip()
    return out


def create_FFTs(dataset):
    out = ''
    junk, dataset_prefix, dataset_middle, dataset_suffix = dataset.split('/')
    dataset_version = dataset_middle[dataset_middle.index('PU_S13'):]
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*_%s_*txt' % (dataset_prefix, dataset_version))
    filenames.sort()
    nb_total = len(filenames)
    for nb_dataset, filename in enumerate(filenames):
        out += TEMPLATE_FFT % {
            'dataset': dataset,
            'filename': filename.replace('./inputs/eos-file-indexes/', ''),
            'nb_dataset': str(nb_dataset + 1),
            'nb_total': str(nb_total)
        }
    return out.rstrip()


def get_version(dataset):
    if dataset in ['ForwardTriggers',]:
        return '2'
    else:
        return '1'


def get_nb_files(dataset):
    out = 0
    filenames = glob.glob('*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        for line in open(filename, 'r').readlines():
            match = re.search(r'<subfield code="s">([0-9]+)</subfield>', line)
            if match:
               out += 1
    return out


def get_nb_bytes(dataset):
    out = 0
    filenames = glob.glob('*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        for line in open(filename, 'r').readlines():
            match = re.search(r'<subfield code="s">([0-9]+)</subfield>', line)
            if match:
               out += int(match.groups()[0])
    return out


def get_doi(recid):
    dois = {
        1300: '10.7483/OPENDATA.CMS.VPJH.JZHB',
        1301: '10.7483/OPENDATA.CMS.V6AN.FXJJ',
        1302: '10.7483/OPENDATA.CMS.GA4B.CKA7',
        1303: '10.7483/OPENDATA.CMS.9MHK.R9U4',
        1304: '10.7483/OPENDATA.CMS.D72N.TR5C',
        1305: '10.7483/OPENDATA.CMS.5YJP.R4GT',
        1306: '10.7483/OPENDATA.CMS.FMNR.TQP3',
        1307: '10.7483/OPENDATA.CMS.ZPH2.MXP5',
        1308: '10.7483/OPENDATA.CMS.HJYH.UMWG',
        1309: '10.7483/OPENDATA.CMS.MQ7E.J9NE',
        1310: '10.7483/OPENDATA.CMS.KUMT.WEYE',
        1311: '10.7483/OPENDATA.CMS.UB82.2FZU',
        1312: '10.7483/OPENDATA.CMS.M5CN.BTGB',
        1313: '10.7483/OPENDATA.CMS.2JTU.TNBJ',
        1314: '10.7483/OPENDATA.CMS.EPE5.ZUXC',
        1315: '10.7483/OPENDATA.CMS.9RHV.X49V',
        1316: '10.7483/OPENDATA.CMS.HKCE.U6EM',
        1317: '10.7483/OPENDATA.CMS.FCES.39BQ',
        1318: '10.7483/OPENDATA.CMS.QKZU.PZQ6',
        1319: '10.7483/OPENDATA.CMS.4W5F.MMUP',
        1320: '10.7483/OPENDATA.CMS.JG6J.FHZY',
        1321: '10.7483/OPENDATA.CMS.UYU2.WCAG',
        1322: '10.7483/OPENDATA.CMS.5KC9.YA5J',
        1323: '10.7483/OPENDATA.CMS.PK4V.5EUK',
        1324: '10.7483/OPENDATA.CMS.D3JK.78CF',
        1325: '10.7483/OPENDATA.CMS.BY94.Z63F',
        1326: '10.7483/OPENDATA.CMS.CK2Q.STKY',
        1327: '10.7483/OPENDATA.CMS.CNRK.R8J7',
        1328: '10.7483/OPENDATA.CMS.RRK8.3ZSV',
        1329: '10.7483/OPENDATA.CMS.BGSX.JJTM',
        1330: '10.7483/OPENDATA.CMS.CR5X.YVQN',
        1331: '10.7483/OPENDATA.CMS.FZAJ.JFW7',
        1332: '10.7483/OPENDATA.CMS.U683.H59F',
        1333: '10.7483/OPENDATA.CMS.TJV5.RZM3',
        1334: '10.7483/OPENDATA.CMS.6QJD.ZDHJ',
        1335: '10.7483/OPENDATA.CMS.JRWG.74V6',
        1336: '10.7483/OPENDATA.CMS.446C.HV8G',
        1337: '10.7483/OPENDATA.CMS.NVP4.XMYR',
        1338: '10.7483/OPENDATA.CMS.P4HX.J233',
        1339: '10.7483/OPENDATA.CMS.X5EZ.K2ZR',
        1340: '10.7483/OPENDATA.CMS.2QR5.9P6G',
        1341: '10.7483/OPENDATA.CMS.KH7Q.Q67U',
        1342: '10.7483/OPENDATA.CMS.96U2.3YAH',
        1343: '10.7483/OPENDATA.CMS.57TZ.6Z9Q',
        1344: '10.7483/OPENDATA.CMS.AGBK.K9CX',
        1345: '10.7483/OPENDATA.CMS.AYFR.VX72',
        1346: '10.7483/OPENDATA.CMS.AGGR.9TEK',
        1347: '10.7483/OPENDATA.CMS.DNZB.34U3',
        1348: '10.7483/OPENDATA.CMS.QJND.HA88',
        1349: '10.7483/OPENDATA.CMS.34MQ.7N72',
        1350: '10.7483/OPENDATA.CMS.3R3P.5JYR',
        1351: '10.7483/OPENDATA.CMS.D2RV.NB9M',
        1352: '10.7483/OPENDATA.CMS.NKM7.VS8G',
        1353: '10.7483/OPENDATA.CMS.2X8H.237F',
        1354: '10.7483/OPENDATA.CMS.PTR7.4RER',
        1355: '10.7483/OPENDATA.CMS.BN7K.8N4A',
        1356: '10.7483/OPENDATA.CMS.WEE7.MUNW',
        1357: '10.7483/OPENDATA.CMS.TZH7.EFE7',
        1358: '10.7483/OPENDATA.CMS.MXSE.G54G',
        1359: '10.7483/OPENDATA.CMS.8E2V.PX7B',
        1360: '10.7483/OPENDATA.CMS.CSJG.AWBA',
        1361: '10.7483/OPENDATA.CMS.7BD2.8XD2',
        1362: '10.7483/OPENDATA.CMS.448D.ZHNC',
        1363: '10.7483/OPENDATA.CMS.466D.T3D9',
        1364: '10.7483/OPENDATA.CMS.RC9V.B5KX',
        1365: '10.7483/OPENDATA.CMS.5NPW.3HWE',
        1366: '10.7483/OPENDATA.CMS.RSKY.VC8C',
        1367: '10.7483/OPENDATA.CMS.P9Z6.X85N',
        1368: '10.7483/OPENDATA.CMS.2K8R.VJJH',
        1369: '10.7483/OPENDATA.CMS.WKRR.DCJP',
        1370: '10.7483/OPENDATA.CMS.CX2X.J3KW',
        1371: '10.7483/OPENDATA.CMS.R5SH.7ZY2',
        1372: '10.7483/OPENDATA.CMS.K64Z.CP2F',
        1373: '10.7483/OPENDATA.CMS.EMGG.EKKB',
        1374: '10.7483/OPENDATA.CMS.HC3V.2QBD',
        1375: '10.7483/OPENDATA.CMS.P6U8.T9N8',
        1376: '10.7483/OPENDATA.CMS.JPW9.E5HW',
        1377: '10.7483/OPENDATA.CMS.6UGA.H7QV',
        1378: '10.7483/OPENDATA.CMS.BYY5.YKS5',
        1379: '10.7483/OPENDATA.CMS.GHZE.S4M3',
        1380: '10.7483/OPENDATA.CMS.VP6H.AWDC',
        1381: '10.7483/OPENDATA.CMS.AZW4.R2GG',
        1382: '10.7483/OPENDATA.CMS.7G2E.4PGB',
        1383: '10.7483/OPENDATA.CMS.ZCNM.27A3',
        1384: '10.7483/OPENDATA.CMS.WK2P.WZSF',
        1385: '10.7483/OPENDATA.CMS.25XG.XPSU',
        1386: '10.7483/OPENDATA.CMS.E8VC.3JS5',
        1387: '10.7483/OPENDATA.CMS.DV6X.5SGW',
        1388: '10.7483/OPENDATA.CMS.2JK2.HTVJ',
        1389: '10.7483/OPENDATA.CMS.U6JT.SMMC',
        1390: '10.7483/OPENDATA.CMS.4G5S.44WQ',
        1391: '10.7483/OPENDATA.CMS.D5KD.U5MR',
        1392: '10.7483/OPENDATA.CMS.UUG7.4NHT',
        1393: '10.7483/OPENDATA.CMS.T8RZ.D52D',
        1394: '10.7483/OPENDATA.CMS.4475.SSXE',
        1395: '10.7483/OPENDATA.CMS.TXT4.4RRP',
        1396: '10.7483/OPENDATA.CMS.PKN9.A4F4',
        1397: '10.7483/OPENDATA.CMS.WJ99.85PE',
        1398: '10.7483/OPENDATA.CMS.5E6B.Q3MJ',
        1399: '10.7483/OPENDATA.CMS.AGZZ.26HG',
        1400: '10.7483/OPENDATA.CMS.DWBP.WWWZ',
        1401: '10.7483/OPENDATA.CMS.44RZ.E298',
        1402: '10.7483/OPENDATA.CMS.MFHX.N8UZ',
        1403: '10.7483/OPENDATA.CMS.JG5S.UCWE',
        1404: '10.7483/OPENDATA.CMS.AD9J.A8ZY',
        1405: '10.7483/OPENDATA.CMS.6PZJ.YEYN',
        1406: '10.7483/OPENDATA.CMS.K8YT.RH62',
        1407: '10.7483/OPENDATA.CMS.UA4D.XGRQ',
        1408: '10.7483/OPENDATA.CMS.9WT8.WCNQ',
        1409: '10.7483/OPENDATA.CMS.YPVY.T53Z',
        1410: '10.7483/OPENDATA.CMS.JV8S.DCSK',
        1411: '10.7483/OPENDATA.CMS.566N.P583',
        1412: '10.7483/OPENDATA.CMS.E85J.TK3G',
        1413: '10.7483/OPENDATA.CMS.S45A.U3CR',
        1414: '10.7483/OPENDATA.CMS.3T6G.QCWD',
        1415: '10.7483/OPENDATA.CMS.GFC7.JB6P',
        1416: '10.7483/OPENDATA.CMS.YGNF.8NP7',
        1417: '10.7483/OPENDATA.CMS.GU9E.KN89',
        1418: '10.7483/OPENDATA.CMS.WCT5.U54E',
        1419: '10.7483/OPENDATA.CMS.6M5H.WRYA',
        1420: '10.7483/OPENDATA.CMS.JV26.YXEA',
        1421: '10.7483/OPENDATA.CMS.C4W8.ENKU',
        1422: '10.7483/OPENDATA.CMS.X8CT.GS2X',
        1423: '10.7483/OPENDATA.CMS.P54T.CSJS',
        1424: '10.7483/OPENDATA.CMS.YSTQ.AYGQ',
        1425: '10.7483/OPENDATA.CMS.SKKX.D34G',
        1426: '10.7483/OPENDATA.CMS.S7NK.ZK8U',
        1427: '10.7483/OPENDATA.CMS.H437.HAQB',
        1428: '10.7483/OPENDATA.CMS.ZASR.7BEP',
        1429: '10.7483/OPENDATA.CMS.CFVD.W4HF',
        1430: '10.7483/OPENDATA.CMS.EZJS.9PZA',
        1431: '10.7483/OPENDATA.CMS.EPUN.P56F',
        1432: '10.7483/OPENDATA.CMS.PJSX.D6DN',
        1433: '10.7483/OPENDATA.CMS.V3VD.KPV5',
        1434: '10.7483/OPENDATA.CMS.UMWW.RPZN',
        1435: '10.7483/OPENDATA.CMS.AUT8.MD6N',
        1436: '10.7483/OPENDATA.CMS.K2MK.P4GY',
        1437: '10.7483/OPENDATA.CMS.5VHJ.9NM3',
        1438: '10.7483/OPENDATA.CMS.9RXN.W3PT',
        1439: '10.7483/OPENDATA.CMS.2ZMR.GBW5',
        1440: '10.7483/OPENDATA.CMS.EEY2.9Y2U',
        1441: '10.7483/OPENDATA.CMS.MPUZ.TBZK',
        1442: '10.7483/OPENDATA.CMS.GWRW.TZ86',
        1443: '10.7483/OPENDATA.CMS.G4SB.Y2BX',
        1444: '10.7483/OPENDATA.CMS.8XNT.2XRX',
        1445: '10.7483/OPENDATA.CMS.DRDE.DFZA',
        1446: '10.7483/OPENDATA.CMS.C8MG.CVMR',
        1447: '10.7483/OPENDATA.CMS.GQG8.72PH',
        1448: '10.7483/OPENDATA.CMS.C2EZ.E8TN',
        1449: '10.7483/OPENDATA.CMS.MDXY.CUAJ',
        1450: '10.7483/OPENDATA.CMS.DXGT.MJGD',
        1451: '10.7483/OPENDATA.CMS.4QNQ.86MW',
        1452: '10.7483/OPENDATA.CMS.9WHE.UE26',
        1453: '10.7483/OPENDATA.CMS.8QK3.83V9',
        1454: '10.7483/OPENDATA.CMS.DENC.DHVT',
        1455: '10.7483/OPENDATA.CMS.J48K.6VMY',
        1456: '10.7483/OPENDATA.CMS.UNTH.MX69',
        1457: '10.7483/OPENDATA.CMS.FX3M.49C6',
        1458: '10.7483/OPENDATA.CMS.3W3N.DX7X',
        1459: '10.7483/OPENDATA.CMS.QZ66.35WA',
        1460: '10.7483/OPENDATA.CMS.KPWJ.6M93',
        1461: '10.7483/OPENDATA.CMS.VYCM.5UT6',
        1462: '10.7483/OPENDATA.CMS.H375.RGYJ',
        1463: '10.7483/OPENDATA.CMS.YY2Y.EQ9E',
        1464: '10.7483/OPENDATA.CMS.K9ED.PD36',
        1465: '10.7483/OPENDATA.CMS.A8UU.6R88',
        1466: '10.7483/OPENDATA.CMS.EFVZ.663S',
        1467: '10.7483/OPENDATA.CMS.7WRD.KQUR',
        1468: '10.7483/OPENDATA.CMS.JEZ4.4ZZS',
        1469: '10.7483/OPENDATA.CMS.X3XQ.USQR',
        1470: '10.7483/OPENDATA.CMS.PE7B.23XG',
        1471: '10.7483/OPENDATA.CMS.CZPT.843Y',
        1472: '10.7483/OPENDATA.CMS.T4MG.3GJC',
        1473: '10.7483/OPENDATA.CMS.WZ2J.Y5B2',
        1474: '10.7483/OPENDATA.CMS.4NZC.69BR',
        1475: '10.7483/OPENDATA.CMS.WZJR.DEYH',
        1476: '10.7483/OPENDATA.CMS.TPNT.6PYK',
        1477: '10.7483/OPENDATA.CMS.K8X4.NNGC',
        1478: '10.7483/OPENDATA.CMS.DMQP.VWE9',
        1479: '10.7483/OPENDATA.CMS.274Q.PNTF',
        1480: '10.7483/OPENDATA.CMS.AD5H.5SVP',
        1481: '10.7483/OPENDATA.CMS.YGD3.HSPT',
        1482: '10.7483/OPENDATA.CMS.Q4M9.UVJN',
        1483: '10.7483/OPENDATA.CMS.Z6PA.3Z5K',
        1484: '10.7483/OPENDATA.CMS.FB4K.G8ZF',
        1485: '10.7483/OPENDATA.CMS.YQNF.2PTX',
        1486: '10.7483/OPENDATA.CMS.ZYMN.WQRP',
        1487: '10.7483/OPENDATA.CMS.SZWT.H9MC',
        1488: '10.7483/OPENDATA.CMS.6K25.N4HP',
        1489: '10.7483/OPENDATA.CMS.FVJE.FT4R',
        1490: '10.7483/OPENDATA.CMS.MQBV.53VN',
        1491: '10.7483/OPENDATA.CMS.BKTE.D4WG',
        1492: '10.7483/OPENDATA.CMS.SGVW.KQY2',
        1493: '10.7483/OPENDATA.CMS.ZVP5.ZHCN',
        1494: '10.7483/OPENDATA.CMS.7M6H.92RR',
        1495: '10.7483/OPENDATA.CMS.4XCW.MVRR',
        1496: '10.7483/OPENDATA.CMS.ANHK.PC9F',
        1497: '10.7483/OPENDATA.CMS.F9K9.3JFC',
        1498: '10.7483/OPENDATA.CMS.UMPG.E6HN',
        1499: '10.7483/OPENDATA.CMS.6TNM.5YPM',
        1500: '10.7483/OPENDATA.CMS.P4E7.SYG5',
        1501: '10.7483/OPENDATA.CMS.45EN.Z925',
        1502: '10.7483/OPENDATA.CMS.WSBR.SUNJ',
        1503: '10.7483/OPENDATA.CMS.VGWV.J3UC',
        1504: '10.7483/OPENDATA.CMS.7K7C.UMET',
        1505: '10.7483/OPENDATA.CMS.YYEE.6MPY',
        1506: '10.7483/OPENDATA.CMS.DBZT.4AZ6',
        1507: '10.7483/OPENDATA.CMS.K9EW.KRDS',
        1508: '10.7483/OPENDATA.CMS.JE22.RQ5J',
        1509: '10.7483/OPENDATA.CMS.496E.7BVA',
        1510: '10.7483/OPENDATA.CMS.VAHX.5WHS',
        1511: '10.7483/OPENDATA.CMS.GFKH.PH6Y',
        1512: '10.7483/OPENDATA.CMS.SZKA.ERNS',
        1513: '10.7483/OPENDATA.CMS.FR3C.3BZX',
        1514: '10.7483/OPENDATA.CMS.TPBS.77DC',
        1515: '10.7483/OPENDATA.CMS.FX8Y.YFTT',
        1516: '10.7483/OPENDATA.CMS.S4FG.DM8Y',
        1517: '10.7483/OPENDATA.CMS.K59T.T7V3',
        1518: '10.7483/OPENDATA.CMS.5UTX.X5U7',
        1519: '10.7483/OPENDATA.CMS.WY8C.B9A5',
        1520: '10.7483/OPENDATA.CMS.QV9U.GCS7',
        1521: '10.7483/OPENDATA.CMS.KW3V.6B3S',
        1522: '10.7483/OPENDATA.CMS.M8Y3.EHUC',
        1523: '10.7483/OPENDATA.CMS.YD32.QVWD',
        1524: '10.7483/OPENDATA.CMS.54YJ.6M72',
        1525: '10.7483/OPENDATA.CMS.55JN.R5JH',
        1526: '10.7483/OPENDATA.CMS.WJSD.P4ET',
        1527: '10.7483/OPENDATA.CMS.KS7P.TDC7',
        1528: '10.7483/OPENDATA.CMS.TUTH.HDWQ',
        1529: '10.7483/OPENDATA.CMS.E5PB.5JXM',
        1530: '10.7483/OPENDATA.CMS.PRK8.9HPT',
        1531: '10.7483/OPENDATA.CMS.2GVF.QYV5',
        1532: '10.7483/OPENDATA.CMS.C6C3.WVKB',
        1533: '10.7483/OPENDATA.CMS.WA6F.6PP7',
        1534: '10.7483/OPENDATA.CMS.5RG6.NNDK',
        1535: '10.7483/OPENDATA.CMS.NGMR.3734',
        1536: '10.7483/OPENDATA.CMS.9WR5.454D',
        1537: '10.7483/OPENDATA.CMS.P6B9.Z7SK',
        1538: '10.7483/OPENDATA.CMS.U3DR.GNRZ',
        1539: '10.7483/OPENDATA.CMS.Q3BX.69VQ',
        1540: '10.7483/OPENDATA.CMS.FSMU.EQHG',
        1541: '10.7483/OPENDATA.CMS.2KY2.4T48',
        1542: '10.7483/OPENDATA.CMS.SRSZ.C6XC',
        1543: '10.7483/OPENDATA.CMS.X7DE.P5GJ',
        1544: '10.7483/OPENDATA.CMS.ZBGF.H543',
        1545: '10.7483/OPENDATA.CMS.6CWA.JUW2',
        1546: '10.7483/OPENDATA.CMS.VTKQ.J8B7',
        1547: '10.7483/OPENDATA.CMS.2Z2V.EF7N',
        1548: '10.7483/OPENDATA.CMS.QH9R.SCTN',
        1549: '10.7483/OPENDATA.CMS.CARQ.ZYN6',
        1550: '10.7483/OPENDATA.CMS.8KEK.TM28',
        1551: '10.7483/OPENDATA.CMS.RYHH.BH37',
        1552: '10.7483/OPENDATA.CMS.X9KD.4XT7',
        1553: '10.7483/OPENDATA.CMS.BKTD.SGJX',
        1554: '10.7483/OPENDATA.CMS.V53F.8KR4',
        1555: '10.7483/OPENDATA.CMS.84VC.RU8W',
        1556: '10.7483/OPENDATA.CMS.972P.PY4C',
        1557: '10.7483/OPENDATA.CMS.3FQQ.KTS6',
        1558: '10.7483/OPENDATA.CMS.EJT7.KSAY',
        1559: '10.7483/OPENDATA.CMS.BUG8.SW65',
        1560: '10.7483/OPENDATA.CMS.S3D5.KF2C',
        1561: '10.7483/OPENDATA.CMS.SMGE.ACWS',
        1562: '10.7483/OPENDATA.CMS.PUTE.7H2H',
        1563: '10.7483/OPENDATA.CMS.N3RG.2JM7',
        1564: '10.7483/OPENDATA.CMS.AHB7.MRSZ',
        1565: '10.7483/OPENDATA.CMS.BW53.8D8E',
        1566: '10.7483/OPENDATA.CMS.S3MW.PQD7',
        1567: '10.7483/OPENDATA.CMS.AS5B.AHYT',
        1568: '10.7483/OPENDATA.CMS.ZBRH.87CA',
        1569: '10.7483/OPENDATA.CMS.AN8T.8KD6',
        1570: '10.7483/OPENDATA.CMS.GRVM.SMAJ',
        1571: '10.7483/OPENDATA.CMS.8SWS.TSW9',
        1572: '10.7483/OPENDATA.CMS.EWAE.G37G',
        1573: '10.7483/OPENDATA.CMS.EG44.NUAB',
        1574: '10.7483/OPENDATA.CMS.N4ZH.FZ6H',
        1575: '10.7483/OPENDATA.CMS.JC4Y.UX8Z',
        1576: '10.7483/OPENDATA.CMS.XVMZ.QX3Q',
        1577: '10.7483/OPENDATA.CMS.PTRW.XFGC',
        1578: '10.7483/OPENDATA.CMS.4CTX.T6S6',
        1579: '10.7483/OPENDATA.CMS.K9BP.QJ7P',
        1580: '10.7483/OPENDATA.CMS.E7AD.YR82',
        1581: '10.7483/OPENDATA.CMS.EU6J.F4P7',
        1582: '10.7483/OPENDATA.CMS.AMM3.D89B',
        1583: '10.7483/OPENDATA.CMS.4PMB.42GH',
        1584: '10.7483/OPENDATA.CMS.XVN9.JU8Y',
        1585: '10.7483/OPENDATA.CMS.GF4R.PRT2',
        1586: '10.7483/OPENDATA.CMS.Q8CE.3CJQ',
        1587: '10.7483/OPENDATA.CMS.D7BJ.BYEG',
        1588: '10.7483/OPENDATA.CMS.HXNW.6KKK',
        1589: '10.7483/OPENDATA.CMS.73DT.ASJS',
        1590: '10.7483/OPENDATA.CMS.NKYE.HJK9',
        1591: '10.7483/OPENDATA.CMS.CG8H.BYSK',
        1592: '10.7483/OPENDATA.CMS.CYDJ.SRGR',
        1593: '10.7483/OPENDATA.CMS.BY6Y.7XG9',
        1594: '10.7483/OPENDATA.CMS.8Z65.HCQP',
        1595: '10.7483/OPENDATA.CMS.WUTT.HEVB',
        1596: '10.7483/OPENDATA.CMS.PPG2.SMMR',
        1597: '10.7483/OPENDATA.CMS.RS4N.ASTQ',
        1598: '10.7483/OPENDATA.CMS.QFGX.WD6P',
        1599: '10.7483/OPENDATA.CMS.8AXG.MKR4',
        1600: '10.7483/OPENDATA.CMS.3SK5.62JZ',
        1601: '10.7483/OPENDATA.CMS.2JNC.K65J',
        1602: '10.7483/OPENDATA.CMS.C92E.U2AH',
        1603: '10.7483/OPENDATA.CMS.JAKG.T248',
        1604: '10.7483/OPENDATA.CMS.87NH.MW74',
        1605: '10.7483/OPENDATA.CMS.79TB.DPW8',
        1606: '10.7483/OPENDATA.CMS.E2SY.QM37',
        1607: '10.7483/OPENDATA.CMS.EZKX.D9AU',
        1608: '10.7483/OPENDATA.CMS.VDSC.RMYB',
        1609: '10.7483/OPENDATA.CMS.P5A8.MRQN',
        1610: '10.7483/OPENDATA.CMS.M8SR.A4GR',
        1611: '10.7483/OPENDATA.CMS.YZXV.3KB9',
        1612: '10.7483/OPENDATA.CMS.QKJW.BJGY',
        1613: '10.7483/OPENDATA.CMS.UY5P.JH9H',
        1614: '10.7483/OPENDATA.CMS.7CGC.HQQF',
        1615: '10.7483/OPENDATA.CMS.PZWS.FCZH',
        1616: '10.7483/OPENDATA.CMS.2UW6.KY6M',
        1617: '10.7483/OPENDATA.CMS.NPGP.5JH9',
        1618: '10.7483/OPENDATA.CMS.B7AU.EP94',
        1619: '10.7483/OPENDATA.CMS.QEMB.3WV2',
        1620: '10.7483/OPENDATA.CMS.S976.NCGF',
        1621: '10.7483/OPENDATA.CMS.25UM.SHS8',
        1622: '10.7483/OPENDATA.CMS.3F4C.YEE5',
        1623: '10.7483/OPENDATA.CMS.X4WM.EDRT',
        1624: '10.7483/OPENDATA.CMS.GQHR.SEQF',
        1625: '10.7483/OPENDATA.CMS.J44N.S7SU',
        1626: '10.7483/OPENDATA.CMS.W9KY.C8C9',
        1627: '10.7483/OPENDATA.CMS.AGS4.CBN8',
        1628: '10.7483/OPENDATA.CMS.PPAU.YSMN',
        1629: '10.7483/OPENDATA.CMS.8V6Q.F7TN',
        1630: '10.7483/OPENDATA.CMS.69AS.YDUF',
        1631: '10.7483/OPENDATA.CMS.PVMZ.QEYQ',
        1632: '10.7483/OPENDATA.CMS.UM9N.54X2',
        1633: '10.7483/OPENDATA.CMS.U7P6.CKVB',
        1634: '10.7483/OPENDATA.CMS.3H7E.UVVA',
        1635: '10.7483/OPENDATA.CMS.W32C.8MSV',
        1636: '10.7483/OPENDATA.CMS.M6DQ.SB9N',
        1637: '10.7483/OPENDATA.CMS.CE6Y.X78E',
        1638: '10.7483/OPENDATA.CMS.AYNJ.DVM3',
        1639: '10.7483/OPENDATA.CMS.Q2TQ.ZVF6',
        1640: '10.7483/OPENDATA.CMS.JCDC.9CUH',
        1641: '10.7483/OPENDATA.CMS.RNK8.M6NR',
        1642: '10.7483/OPENDATA.CMS.74ZB.STJC',
        1643: '10.7483/OPENDATA.CMS.236Q.R8TQ',
        1644: '10.7483/OPENDATA.CMS.FHQF.BQ53',
        1645: '10.7483/OPENDATA.CMS.4TQG.Q2SY',
        1646: '10.7483/OPENDATA.CMS.5GG4.DBJ5',
        1647: '10.7483/OPENDATA.CMS.FG73.WJ46',
        1648: '10.7483/OPENDATA.CMS.95DX.4BMP',
        1649: '10.7483/OPENDATA.CMS.6FGH.RMKT',
        1650: '10.7483/OPENDATA.CMS.BF8Y.7WSJ',
        1651: '10.7483/OPENDATA.CMS.XWVK.M4VG',
        1652: '10.7483/OPENDATA.CMS.UHTP.T7WF',
        1653: '10.7483/OPENDATA.CMS.SHE7.2B6V',
        1654: '10.7483/OPENDATA.CMS.4C7T.ABQB',
        1655: '10.7483/OPENDATA.CMS.8WEU.B6D8',
        1656: '10.7483/OPENDATA.CMS.39DX.GD5E',
        1657: '10.7483/OPENDATA.CMS.6R4H.NHMN',
        1658: '10.7483/OPENDATA.CMS.B2CK.Q4AQ',
        1659: '10.7483/OPENDATA.CMS.9BT8.5DRB',
        1660: '10.7483/OPENDATA.CMS.EG8Z.8AFD',
        1661: '10.7483/OPENDATA.CMS.FGDH.9YJ9',
        1662: '10.7483/OPENDATA.CMS.VNS2.C226',
        1663: '10.7483/OPENDATA.CMS.ZKQ8.NRMD',
        1664: '10.7483/OPENDATA.CMS.2AEX.34VT',
        1665: '10.7483/OPENDATA.CMS.7D6V.YTKX',
        1666: '10.7483/OPENDATA.CMS.PTSP.YCQ7',
        1667: '10.7483/OPENDATA.CMS.QNZU.CCWV',
        1668: '10.7483/OPENDATA.CMS.N4B2.4DKV',
        1669: '10.7483/OPENDATA.CMS.89DA.G2QV',
        1670: '10.7483/OPENDATA.CMS.G6N5.S9CE',
        1671: '10.7483/OPENDATA.CMS.KZV6.W86V',
        1672: '10.7483/OPENDATA.CMS.GHZE.PZER',
        1673: '10.7483/OPENDATA.CMS.MVVE.33HX',
        1674: '10.7483/OPENDATA.CMS.HB9Y.8B4H',
        1675: '10.7483/OPENDATA.CMS.Q7MA.G5CR',
        1676: '10.7483/OPENDATA.CMS.PM7G.7PGC',
        1677: '10.7483/OPENDATA.CMS.4TH5.SVD6',
        1678: '10.7483/OPENDATA.CMS.A354.RGSQ',
        1679: '10.7483/OPENDATA.CMS.A5DW.6RSE',
        1680: '10.7483/OPENDATA.CMS.4GWY.M6BX',
    }
    return dois[recid]


def get_category(title):
    """Guess category for the title."""
    title_lower = title.lower()

    if 'lambda' in title_lower or \
       'Bu' in title or \
       'Bd' in title or \
       'jpsi' in title_lower or \
       'upsilon' in title_lower:
        return 'B-physics'

    elif 'higgs2p' in title_lower or \
         'bsm' in title_lower or \
         'graviton2' in title_lower or \
         'higgs0' in title_lower:
        return 'BSM Higgs'

    elif 'matchingup' in title_lower or \
         'matchingdown' in title_lower or \
         'scaleup' in title_lower or \
         'scaledown' in title_lower or \
         re.search(r'tt_weights.*auet2', title_lower) or \
         '_mt' in title_lower or \
         '_mass' in title_lower:
        return 'SM Systematic Variations'

    elif 'higgs' in title_lower or \
         'hto' in title_lower or \
         '_hcontin' in title_lower or \
         '_smhcontin' in title_lower or \
         'h_m' in title_lower:
        return 'SM Higgs'

    elif 'HT' in title or \
         'Pt' in title or \
         'enriched' in title_lower or \
         re.search(r'[0-9]jet', title_lower):
        return 'SM Exclusive'

    return 'SM Inclusive'


def get_brief_title(title):
    "Return brief version of the dataset title."
    return title.split("/")[1]


def get_title_heading(title):
    "Return nice title heading for title."
    return "Simulated dataset %s in AODSIM format for 2011 collision data (%s)" % (get_brief_title(title), get_category(title))


def get_generator_text(dataset):
    """Return generator text for given dataset."""
    import os
    from create_config_file_records import get_title as get_generator_title
    from create_config_file_records import get_process
    config_ids = get_from_deep_json(get_das_json(dataset), 'config_id')
    if isinstance(config_ids, str):
        config_ids = [config_ids, ]
    process = ''
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            if process:
                process += ' '
            process += get_process(afile)
    lhe_info_needed = False
    out = '<p>'
    out += '<strong>Step %s</strong>' % process
    out += '<br>Release: %s' % get_from_deep_json(get_das_json(dataset), 'release')
    out += '<br>Global tag: %s' % get_from_deep_json(get_das_json(dataset), 'conditions')
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            generator_text = get_generator_title(afile)
            out += '<br><a href="/record/%s">%s</a>' % (LINK_INFO[config_id], generator_text)
            if 'LHE' in generator_text:
                lhe_info_needed = True
    out += '<br>Output dataset: %s' % dataset
    out += '</p>'
    if lhe_info_needed:
        out += """
        <p><strong>Note</strong>
        <br>
To extract the exact LHE configuration, you can use the following script available in the <a href="/getting-started/CMS">CMS working environment</a> on the <a href="/VM/CMS">CMS Open Data VM</a>:

        <blockquote>
        <pre>
$ dumpLHEHeader.py input=file:somefile.root output=testout.lhe
        </pre>
        </blockquote>

where <code>"somefile.foot"</code> is one of the root files in this dataset.

For example, in the existing working area, you can read the generator information directly from any of the root files of this dataset on the CERN Open Data area (the path to the root files is available from the file index of the record):

        <blockquote>
        <pre>
cd CMSSW_5_3_32/src
cmsenv
dumpLHEHeader.py input=file:root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/TTJets_MSDecays_dileptonic_matchingdown_7TeV-madgraph-tauola/AODSIM/PU_S13_START53_LV6_ext1-v1/60000/0282B13B-490E-E511-8E8A-001E67A3EF70.root output=testout.lhe
        </pre>
        </blockquote>
        </p>
        """
    return """
%s
""" % out


def get_all_generator_text(dataset):
    """Return generator text for given dataset and all its parents."""
    out = '<p>These data were processed in several steps:</p>'
    input_dataset = dataset
    out_blocks = []
    while input_dataset:
        out_blocks.append(get_generator_text(input_dataset))
        input_dataset = get_input_dataset(get_das_json(input_dataset))
    out_blocks.reverse()
    return out + "".join(out_blocks)


def get_number_of_events(das):
    "Return number of events from DAS json."
    return get_from_deep_json(das, 'nevents')


def get_number_of_files(das):
    "Return number of files from DAS json."
    return get_from_deep_json(das, 'nfiles')


def get_number_of_bytes(das):
    "Return number of bytes from DAS json."
    return get_from_deep_json(das, 'size')


def get_cmssw_release(das):
    "Return CMSSW release number from DAS json."
    return get_from_deep_json(das, 'release')


def get_global_tag(das):
    "Return global tagfrom DAS json."
    global_tag = get_from_deep_json(das, 'conditions')
    return global_tag.replace('::All', '')


def get_generators(das):
    "Return string representing list of generators from the DAS json."
    generators = get_from_deep_json(das, 'generators')
    if isinstance(generators, list):
        generators = " ".join(generators)
    return generators


def main():
    """Do the main job."""

    print "<collection>"
    recid = 1300
    for title in open('./inputs/cms-mc-nov-2015.txt', 'r').readlines():
        title = title.strip()
        dataset = title
        das = get_das_json(title)
        print RECORD_TEMPLATE % \
            {
                'recid': str(recid),
                'category': get_category(title),
                'doi': get_doi(recid),
                'dataset': dataset,
                'nb_events': get_number_of_events(das),
                'nb_files': get_number_of_files(das),
                'nb_bytes': get_number_of_bytes(das),
                'cmssw_release': get_cmssw_release(das),
                'generators': get_generators(das),
                'global_tag': get_global_tag(das),
                'title': title,
                'title_heading': get_title_heading(title),
                'raw': title,
                'generator_parameters': '<![CDATA[' + get_all_generator_text(dataset) + ']]>',
                '8567s': create_8567s(dataset),
                'FFTs': create_FFTs(dataset),
            }
        recid += 1
    print "</collection>"


if __name__ == '__main__':
    main()
