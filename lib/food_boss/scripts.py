"""
Simple script to manage recipes.
"""
# core python libraries
import argparse
import logging
# third party libraries
# custom libraries
import food_boss.config


class FoodBossCli(food_boss.config.GlobalConfig):

    def __init__(self):
        self.__init_vars()
        self.__init_root_logger()
        self.__init_cli()

    def __init_vars(self):
        pass

    def __init_root_logger(self):
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
        self.args = self.cli.parse_args()
        if self.args.verbose:
            self.logger.setLevel(logging.DEBUG)
            for h in self.logger.handlers:
                h.setLevel(logging.DEBUG)
            self.logger.debug('Logger reset to debug.')

    def main(self):
        self.logger.debug('Inside main.')
        self.parse_args()

    @staticmethod
    def main_static():
        fbc = FoodBossCli()
        fbc.main()

# End of file.
