from __future__ import annotations
from abc import ABC, abstractmethod
import typing
import numpy as np
import pandas as pd

import langbrainscore

class Encoder(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def encode(self, dataset: 'langbrainscore.dataset.DataSet') -> pd.DataFrame:
        return NotImplemented


class BrainEncoder(Encoder):
    '''
    This class provides a wrapper around real-world brain data of various kinds
        which may be: 
            - neuroimaging [fMRI, PET]
            - physiological [ERP, MEG, ECOG]
            - behavioral [RT, Eye-tracking]
    across several subjects. The class implements `BrainEncoder.encode` which takes in
    a collection of stimuli (typically `np.array` or `list`) 
    '''

    _dataset: langbrainscore.dataset.Dataset = None

    def __init__(self, dataset = None) -> None:
        # if not isinstance(dataset, langbrainscore.dataset.BrainDataset):
        #     raise TypeError(f"dataset must be of type `langbrainscore.dataset.BrainDataset`, not {type(dataset)}")
        self._dataset = dataset

    @property
    def dataset(self) -> langbrainscore.dataset.Dataset:
        return self._dataset

    # @typing.overload
    # def encode(self, stimuli: typing.Union[np.array, list]): ...
    def encode(self, dataset: 'langbrainscore.dataset.BrainDataSet' = None):
        """returns an "encoding" of stimuli (passed in as a BrainDataset)

        Args:
            stimuli (langbrainscore.dataset.BrainDataset):

        Returns:
            pd.DataFrame: neural recordings for each stimulus, multi-indexed 
                          by layer (trivially just 1 layer)
        """        
        
        dataset = dataset or self.dataset

        if (timeid_dims := dataset._dataset.dims['timeid']) > 1:
            return dataset._dataset.mean('timeid')
        elif timeid_dims == 1:
            return dataset._dataset.squeeze('timeid')
        else:
            raise ValueError(f'timeid has invalid shape {timeid_dims}')



class ANNEncoder(Encoder):
    def __init__(self) -> None:
        super().__init__(self)
        pass


    def encode(self, dataset: 'langbrainscore.dataset.DataSet'):
        """[summary]
        
        # Todo: Arguments: embedding method, lower-casing, punctuation (potentially: standardization, outlier removal?)
                Link to HF, only load model of interest 
        
        Args:
            stimuli (langbrainscore.dataset.DataSet): [description]

        Returns:
            pd.DataFrame: neural recordings for each stimulus, multi-indexed according 
                          to the various layers of the ANN model
        """        
        ...

        raise NotImplementedError
        
