# -*- coding: utf-8 -*-
import os
import logging
import click
# from dotenv import find_dotenv, load_dotenv
from random_walker import create_grids, save_hdf5


@click.command()
@click.option('-w', '--width', default=8, type=int)
@click.option('-h', '--height', default=8, type=int)
@click.option('-n', '--num-examples', default=10000, type=int)
@click.option('-p', '--positive-fraction', default=0.5, type=float)
@click.argument('output_filepath', type=click.Path())
def main(width, height, num_examples, positive_fraction, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    grids, steps, connection = create_grids(
        height, width, num_examples, positive_fraction, output_filepath)
    save_hdf5(grids, steps, connection, output_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    main()
