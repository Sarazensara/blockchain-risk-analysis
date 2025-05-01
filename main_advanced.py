from load_data import load_dataset
from analyze_advanced import advanced_frequency_analysis
from visualize import plot_risk_frequencies

risk_columns = [
    'Is_closed_source', 'hidden_owner', 'anti_whale_modifiable',
    'Is_anti_whale', 'Is_honeypot', 'buy_tax', 'sell_tax',
    'slippage_modifiable', 'Is_blacklisted', 'can_take_back_ownership',
    'owner_change_balance', 'is_airdrop_scam', 'selfdestruct', 'trust_list',
    'is_whitelisted', 'is_fake_token', 'illegal_unicode', 'exploitation',
    'bad_contract', 'reusing_state_variable', 'encode_packed_collision',
    'encode_packed_parameters', 'centralized_risk_medium',
    'centralized_risk_high', 'centralized_risk_low', 'event_setter',
    'external_dependencies', 'immutable_states',
    'reentrancy_without_eth_transfer', 'incorrect_inheritance_order',
    'shadowing_local', 'events_maths'
]

if __name__ == '__main__':
    df = load_dataset('/Users/odettesaenz/Downloads/compiled_risk_data.csv')
    if df is not None:
        frequencies = advanced_frequency_analysis(df, risk_columns)
        plot_risk_frequencies(frequencies)