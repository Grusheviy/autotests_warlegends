from altunityrunner import By
from alt_tester_python.base_test_case import BaseTestCase
from wrapper_specific import WrapperSpecific as Wrapper
from testing.cases.chest_open.common.chest_open_utils import ChestOpenUtils
from testing.cases.common.port_command_sender import charge_chest


def battery_chest_open_script(test: BaseTestCase, wrapper: Wrapper):
    account_id = wrapper.get_account_id()
    chest_id = 2090002
    amount = 1

    batteries_amount_before = []
    batteries_amount_in_chest = []
    batteries_amount_after_reward = []

    # Открываем окно с энергией и запоминаем количество батареек
    wrapper.tap_and_check('button_top_bar_hero_energy', [], ['window_battery(Clone)'])

    # Записываем дефолтное количество батареек
    ChestOpenUtils.get_batteries_number(wrapper, batteries_amount_before, 0, 3)

    # Выдаем сундук с батарейками
    charge_chest(wrapper, account_id, chest_id, amount)

    # Открываем сундук
    wrapper.tap_and_check('button_common_rewards_take', ['window_common_rewards(Clone)'], ['window_chestopen(Clone)'])
    wrapper.tap_and_check('button_chestopen_skip_all', ['button_chestopen_skip_all'],
                          ['scrollview_chestopen_rewards_final', 'button_chestopen_take',
                           'text_chestopen_chests_count'])

    # Запоминаем количество каждой из батареек (с большой до маленькой)
    rewards_list = wrapper.altdriver.find_objects(
        By.PATH, '//scrollview_chestopen_rewards_final/panel_chestopen_rewards_final_viewport/'
                 'panel_chestopen_rewards_final_content/item_chestopen_reward_final(Clone)')
    for count_reward_in_list, reward_in_list in reversed(list(enumerate(rewards_list))):
        batteries_amount = (wrapper.altdriver.find_objects(
            By.PATH, "//panel_chestopen_rewards_final_viewport/panel_chestopen_rewards_final_content//"
                     "panel_item_common_reward_place/*")[count_reward_in_list].name.split('amount=')[1].split('}')[0])
        batteries_amount_in_chest.append(batteries_amount)
        wrapper.sleep(1)

    # Забираем награду из сундука
    wrapper.tap_and_check('button_chestopen_take', ['scrollview_chestopen_rewards_final', 'button_chestopen_take',
                                                    'text_chestopen_chests_count'], [])

    # Проверяем, что полученные из сундука батарейки появились у игрока
    try:
        for batteries_count in range(3):
            wrapper.wait_until(lambda wrapper: (wrapper.wait_object_and_get_text(
                    By.PATH, f"//panel_battery_goods_layout[{batteries_count}]//text_good_hint").split("5>")[1]),
                                batteries_amount_in_chest[batteries_count], timeout=1)
            batteries_amount_after_reward.append(wrapper.wait_object_and_get_text(
                    By.PATH, f"//panel_battery_goods_layout[{batteries_count}]//text_good_hint").split("5>")[1])
    except Exception as e:
        raise Exception(f'The number of cards does not match, batteries amount in chest = {batteries_amount_in_chest}, '
                        f'batteries amount after reward = {batteries_amount_after_reward}', e)

    # Закрываем окно батареек
    wrapper.tap_and_check('button_battery_close', ['window_battery(Clone)'], [])
