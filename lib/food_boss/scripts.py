"""
All CLIs start here using "entry-points".
"""
# core python libraries
import argparse
import logging
# third party libraries
# custom libraries
import food_boss.config


class FoodBossMainCli(food_boss.config.GlobalConfig):

    def __init__(self):
        self.__init_vars()
        self.__init_root_logger()

    def __init_vars(self):
        pass

    def __init_logger(self):
        logging.basicConfig()
        self.logger = logging.getLogger(self.base_logger_name)

    def __init_cli(self):
        self.cli = argparse.ArgumentParser(description=__doc__)
        self.cli.add_argument(
            '--verbose',
            action='store_true',
            help='More output. (DEBUG logging level)'
            )

    def parse_args(self):
        pass

    def main(self):
        self.logger.debug('Inside main.')
        self.parse_args()

# End of file.
