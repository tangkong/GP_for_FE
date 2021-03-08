# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import numpy as np
import pandas as pd

# convert raw to processed
# Intent is to be run from notebooks folder.
def fe_csv_clean(input_filepath, output_filepath,
                dataset_name='FE_HZCO_samples_11-17.csv'):
    rpath = input_filepath + dataset_name
    fe_data = pd.read_csv(rpath, index_col=0)

    fe_data['log(RTA time)'] = np.log(fe_data['RTA time (sec)'])

    fe_data.to_csv(output_path + 'clean_' + dataset_name)


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # process data
    fe_csv_clean(input_filepath, output_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
