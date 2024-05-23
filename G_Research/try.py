# handling exception when input a string, raise customized exception showing "abc"
def auction_bids(game_info, current_info, last_auction_result, player_information):
    round_number = game_info['Round_Number']
    total_items = game_info['Total_Number_Items']
    robots = game_info['Number_Robots']
    remaining_items = current_info['Remaining_Number_Items']
    current_vp = current_info['vp']
    current_budget = current_info['remaining_budget']
    last_winner = last_auction_result['winner']
    last_winning_bid = last_auction_result['winning_bid']
    last_vp = last_auction_result['vp']
    last_total_bid = last_auction_result['total']
    last_min_bid = last_auction_result['min']
    robots_name = ['Robot_' + str(i+1) for i in range(robots)]

    if remaining_items != 0:
        player_information[remaining_items] = {'game_info': game_info, 'current_info': current_info, 'last_auction_result': last_auction_result, 'player_information': player_information}
        return 0
    else:
        raise Exception(player_information)
    

    
37: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
             'current_info': {'Remaining_Number_Items': 37, 'vp': 0.2697867137638703, 'remaining_budget': 1}, 
             'last_auction_result': {'winner': None, 'winning_bid': None, 'vp': None, 'total': None, 'min': None}}, 

36: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 36, 'vp': 0.04097352393619469, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027224095478498075, 'min': 0.0, 'vp': 0.2697867137638703}},

35: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 35, 'vp': 0.016527635528529094, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027027027024324322, 'min': 0.0, 'vp': 0.04097352393619469}}, 

34: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 34, 'vp': 0.8132702392002724, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027027027024324322, 'min': 0.0, 'vp': 0.016527635528529094}}, 

33: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 33, 'vp': 0.9127555772777217, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.4089419371304637, 'min': 0.0, 'vp': 0.8132702392002724}}, 

32: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 32, 'vp': 0.6066357757671799, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.39943882572895706, 'min': 0.0, 'vp': 0.9127555772777217}}, 

31: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 31, 'vp': 0.7294965609839984, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_2', 'winning_bid': 0.05263157894210526, 'total': 0.07965860596642958, 'min': 0.0, 'vp': 0.6066357757671799}}, 

30: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 30, 'vp': 0.5436249914654229, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.2994388257389571, 'min': 0.0, 'vp': 0.7294965609839984}}, 
     
29: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
          'current_info': {'Remaining_Number_Items': 29, 'vp': 0.9350724237877682, 'remaining_budget': 1}, 
          'last_auction_result': {'winner': 'Robot_2', 'winning_bid': 0.05263157894210526, 'total': 0.07965860596642958, 'min': 0.0, 'vp': 0.5436249914654229}}, 

28: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 28, 'vp': 0.8158535541215322, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.45422784421034057, 'min': 0.0, 'vp': 0.9350724237877682}}, 

27: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 27, 'vp': 0.002738500170148095, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.39943882572895706, 'min': 0.0, 'vp': 0.8158535541215322}}, 

26: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 26, 'vp': 0.8574042765875693, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027027027024324322, 'min': 0.0, 'vp': 0.002738500170148095}}, 

25: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 25, 'vp': 0.033585575305464355, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.483809883835686, 'min': 0.0, 'vp': 0.8574042765875693}}, 

24: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 24, 'vp': 0.7296554464299441, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027027027024324322, 'min': 0.0, 'vp': 0.033585575305464355}}, 

23: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 23, 'vp': 0.17565562060255901, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_5', 'winning_bid': 0.14285714285714285, 'total': 0.3883530659971889, 'min': 0.0, 'vp': 0.7296554464299441}}, 

22: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 
     'current_info': {'Remaining_Number_Items': 22, 'vp': 0.8631789223498866, 'remaining_budget': 1}, 
     'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027027027024324322, 'min': 0.0, 'vp': 0.17565562060255901}}, 

21: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 21, 'vp': 0.5414612202490917, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_7', 'winning_bid': 0.12303277506372, 'total': 0.37961445793553417, 'min': 0.0, 'vp': 0.8631789223498866}}, 20: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 20, 'vp': 0.2997118905373848, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_2', 'winning_bid': 0.05263157894210526, 'total': 0.07965860596642958, 'min': 0.0, 'vp': 0.5414612202490917}}, 19: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 19, 'vp': 0.42268722119765845, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_7', 'winning_bid': 0.04533956622569419, 'total': 0.07236659325001851, 'min': 0.0, 'vp': 0.2997118905373848}}, 18: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 18, 'vp': 0.028319671145462966, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_7', 'winning_bid': 0.06619145768329568, 'total': 0.09321848470762001, 'min': 0.0, 'vp': 0.42268722119765845}}, 17: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 17, 'vp': 0.12428327649956394, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.027027027024324322, 'min': 0.0, 'vp': 0.028319671145462966}}, 16: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 16, 'vp': 0.6706244146936303, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_1', 'winning_bid': 0.027027027024324322, 'total': 0.04815235262266447, 'min': 0.0, 'vp': 0.12428327649956394}}, 15: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 15, 'vp': 0.6471895115742501, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_7', 'winning_bid': 0.1200969325436897, 'total': 0.29792861542550386, 'min': 0.0, 'vp': 0.6706244146936303}}, 14: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 14, 'vp': 0.6153851114812539, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_2', 'winning_bid': 0.05263157894210526, 'total': 0.10640860596642959, 'min': 0.0, 'vp': 0.6471895115742501}}, 13: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 13, 'vp': 0.38367755426188344, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_7', 'winning_bid': 0.10005699856979493, 'total': 0.21196560453622454, 'min': 0.0, 'vp': 0.6153851114812539}}, 12: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 12, 'vp': 0.997209935789211, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.037750000000000006, 'total': 0.06477702702432434, 'min': 0.0, 'vp': 0.38367755426188344}}, 11: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 11, 'vp': 0.9808353387762301, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_7', 'winning_bid': 0.14101854887095044, 'total': 0.4408502317427646, 'min': 0.0, 'vp': 0.997209935789211}}, 10: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 10, 'vp': 0.6855419844806947, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_4', 'winning_bid': 0.09999999999, 'total': 0.3053316828718142, 'min': 0.0, 'vp': 0.9808353387762301}}, 9: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 9, 'vp': 0.6504592762678163, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_3', 'winning_bid': 0.07692307691538461, 'total': 0.2108316828818142, 'min': 0.0, 'vp': 0.6855419844806947}}, 8: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 8, 'vp': 0.6884467305709401, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.05975, 'total': 0.13940860596642957, 'min': 0.0, 'vp': 0.6504592762678163}}, 7: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 7, 'vp': 0.3889214239791038, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_3', 'winning_bid': 0.07692307691538461, 'total': 0.28762260380882754, 'min': 0.0, 'vp': 0.6884467305709401}}, 6: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 6, 'vp': 0.13509650502241122, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.07075000000000001, 'total': 0.09777702702432434, 'min': 0.0, 'vp': 0.3889214239791038}}, 5: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 5, 'vp': 0.7214883401940817, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.07625, 'total': 0.10327702702432431, 'min': 0.0, 'vp': 0.13509650502241122}}, 4: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 4, 'vp': 0.5253543224757259, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.08174999999999999, 'total': 0.15444580169536556, 'min': 0.0, 'vp': 0.7214883401940817}}, 3: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 3, 'vp': 0.31024187555895566, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.08725, 'total': 0.11427702702432432, 'min': 0.0, 'vp': 0.5253543224757259}}, 2: {'game_info': {'Round_Number': 1, 'Total_Number_Items': 37, 'Number_Robots': 7}, 'current_info': {'Remaining_Number_Items': 2, 'vp': 0.4858353588317891, 'remaining_budget': 1}, 'last_auction_result': {'winner': 'Robot_6', 'winning_bid': 0.09275, 'total': 0.11977702702432433, 'min': 0.0, 'vp': 0.31024187555895566}}}