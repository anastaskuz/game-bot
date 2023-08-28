from loguru import logger
from aiogram import executor

from create_bot import DP
from handlers import main_menu_h
from handlers import r_s_p_h
from handlers import coin_toss_h


# хэндлеры
main_menu_h.register_handlers_main(DP)
r_s_p_h.register_handlers_r_s_p(DP)
coin_toss_h.register_handlers_coin_toss(DP)


if __name__ == '__main__':

    logger.info('Запущен бот')
    
    # запуск бота
    # skip_updates - чтобы когда бот вышел из неактивного режима,
    # все пришедшие ему сообщения за это время на него не свалились
    executor.start_polling(DP, skip_updates=True)
    
