from configs.targf_ball_base import get_default_config

def get_config():
    config = get_default_config()
    
    ''' Train GF '''
    # file
    config.data_name = 'CircleCluster_Examples_new_pattern'
    # env
    config.pattern = 'CircleCluster'

    ''' Train SAC '''
    # file 
    config.score_exp = 'CircleCluster_Score_newpattern_largebs'
    # reward
    config.lambda_col = 5.0
    config.lambda_sim = 1.0

    ''' Eval Policy '''
    config.policy_type = 'targf_orca' # ['targf_orca', 'targf_sac']
    config.policy_exp = 'CircleCluster_SAC'
    config.calc_metrics = True
    config.save_videos = True
    # config.test_seeds = [5, 10, 15, 20, 25]
    # config.test_num = 100
    config.test_seeds = [5, 10]
    config.test_num = 8

    return config
