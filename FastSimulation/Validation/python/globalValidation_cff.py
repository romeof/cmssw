import FWCore.ParameterSet.Config as cms

# TrackingParticle-SimHit associator
from SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi import * 
simHitTPAssocProducer.simHitSrc = cms.VInputTag(cms.InputTag('famosSimHits','TrackerHits'),
                                                cms.InputTag("MuonSimHits","MuonCSCHits"),
                                                cms.InputTag("MuonSimHits","MuonDTHits"),
                                                cms.InputTag("MuonSimHits","MuonRPCHits"))

from Validation.RecoMET.METRelValForDQM_cff import *

from Validation.TrackingMCTruth.trackingTruthValidation_cfi import *
from Validation.RecoTrack.TrackValidation_cff import *
from Validation.RecoTrack.TrajectorySeedValidation_cff import *
from Validation.RecoJets.JetValidation_cff import *
from Validation.RecoMuon.muonValidation_cff import *
from Validation.MuonIsolation.MuIsoVal_cff import *
from Validation.MuonIdentification.muonIdVal_cff import *
from Validation.RecoTau.DQMMCValidation_cfi import *
muonIdVal.makeCosmicCompatibilityPlots = False

from Validation.RecoEgamma.egammaValidation_cff import *


from DQMOffline.RecoB.dqmAnalyzer_cff import *


globalPrevalidation = cms.Sequence( 
    simHitTPAssocProducer
    *tracksPreValidation
    *photonPrevalidationSequence
    *produceDenoms
    *prebTagSequenceMC
     )

globalValidation = cms.Sequence(trackingTruthValid
                                +tracksValidation
                                +METRelValSequence
                                +recoMuonValidation
                                +muIsoVal_seq
                                +muonIdValDQMSeq
                                +bTagPlotsMC
                                +egammaValidation
                                +JetValidation
                                +pfTauRunDQMValidation
                                )

globalValidation_preprod = cms.Sequence(trackingTruthValid
                                +tracksValidation
                                +METRelValSequence
                                +recoMuonValidation
                                +muIsoVal_seq
                                +muonIdValDQMSeq
                                )
