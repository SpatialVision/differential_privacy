# -*- coding: utf-8 -*-

"""
/***************************************************************************
 DifferentialPrivacy
                                 A QGIS plugin
 Methods for anonymizing data for public distribution
                              -------------------
        begin                : 2015-11-02
        copyright            : (C) 2015 by Henry Walshaw
        email                : henry.walshaw@spatialvision.com.au
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Henry Walshaw'
__date__ = '2015-11-02'
__copyright__ = '(C) 2015 by Henry Walshaw'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from anon_methods_algorithm import (
    DifferentialPrivacyAlgorithm, DisplacementLines, GridBasedMasking
)
from anon_utils import DifferentialPrivacyUtils


class DifferentialPrivacyProvider(AlgorithmProvider):


    def __init__(self):
        AlgorithmProvider.__init__(self)

        # Deactivate provider by default
        self.activate = False

        # Load algorithms
        self.alglist = [
            DifferentialPrivacyAlgorithm(), DisplacementLines(),
            GridBasedMasking()
        ]
        for alg in self.alglist:
            alg.provider = self


    def initializeSettings(self):
        """In this method we add settings needed to configure our
        provider.

        Do not forget to call the parent method, since it takes care
        or automatically adding a setting for activating or
        deactivating the algorithms in the provider.
        """
        AlgorithmProvider.initializeSettings(self)
        ProcessingConfig.addSetting(Setting(
            self.getDescription(),
            DifferentialPrivacyUtils.DIFFERENTIAL_EPSILON,
            self.tr('Privacy epsilon (higher value gives more privacy)'),
            2.
        ))

    def unload(self):
        """Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        AlgorithmProvider.unload(self)
        ProcessingConfig.removeSetting(
            DifferentialPrivacyUtils.DIFFERENTIAL_EPSILON)

    def getName(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return 'Spatial Vision'

    def getDescription(self):
        """This is the provired full name.
        """
        return 'Differential privacy'

    def getIcon(self):
        """Get the icon.
        """
        return DifferentialPrivacyUtils.getIcon()

    def _loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.algs = self.alglist
