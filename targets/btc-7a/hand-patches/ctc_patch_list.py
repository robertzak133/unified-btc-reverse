## A set of hand created binary patches for the BTC-7A.
## To be consumed by codePatcher() functions

# Hooks for Custom Trail Camera Environment Initalization
ctc_init_patch_list = {}
ctc_init_patch_list['CTC_init_hook'] = {}
ctc_init_patch_list['CTC_init_hook']['start_offset'] = 0x00011af8
ctc_init_patch_list['CTC_init_hook']['change_from_jump']  = 'jal.HceCommon_InitOptions'
ctc_init_patch_list['CTC_init_hook']['change_to_jump'] = 'jal.ctc_init_hook'

# Redirect the call to setup the CodeSentry
ctc_init_patch_list['CTC_code_sentry_call'] = {}
ctc_init_patch_list['CTC_code_sentry_call']['start_offset'] = 0x0000138c
ctc_init_patch_list['CTC_code_sentry_call']['change_from_jump']  = 'jal.initCodeSentry'
ctc_init_patch_list['CTC_code_sentry_call']['change_to_jump'] = 'jal.ctc_initCodeSentry'

