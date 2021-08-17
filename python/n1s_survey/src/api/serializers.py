from rest_framework import serializers

from core.models import *


class EvaluationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        evaluation = Evaluation.objects.create(
            evaluated_person           = validated_data['evaluated_person'],
            line_manager               = validated_data['line_manager'],
            evaluator                  = validated_data['evaluator'],
            survey1_competency_level1  = validated_data['survey1_competency_level1'],
            survey1_competency_level2  = validated_data['survey1_competency_level2'],
            survey1_competency_level3  = validated_data['survey1_competency_level3'],
            survey2_competency_level1  = validated_data['survey2_competency_level1'],
            survey2_competency_level2  = validated_data['survey2_competency_level2'],
            survey3_competency_level1  = validated_data['survey3_competency_level1'],
            survey3_competency_level2  = validated_data['survey3_competency_level2'],
            survey3_competency_level3  = validated_data['survey3_competency_level3'],
            survey3_competency_level4  = validated_data['survey3_competency_level4'],
            survey3_competency_level5  = validated_data['survey3_competency_level5'],
            survey3_competency_level6  = validated_data['survey3_competency_level6'],
            survey3_competency_level7  = validated_data['survey3_competency_level7'],
            survey3_competency_level8  = validated_data['survey3_competency_level8'],
            survey3_competency_level9  = validated_data['survey3_competency_level9'],
            survey3_competency_level10 = validated_data['survey3_competency_level10'],
            survey3_competency_level11 = validated_data['survey3_competency_level11'],
            survey1_grade1             = validated_data['survey1_grade1'],
            survey1_grade2             = validated_data['survey1_grade2'],
            survey1_grade3             = validated_data['survey1_grade3'],
            survey2_grade1             = validated_data['survey2_grade1'],
            survey2_grade2             = validated_data['survey2_grade2'],
            survey3_grade1             = validated_data['survey3_grade1'],
            survey3_grade2             = validated_data['survey3_grade2'],
            survey3_grade3             = validated_data['survey3_grade3'],
            survey3_grade4             = validated_data['survey3_grade4'],
            survey3_grade5             = validated_data['survey3_grade5'],
            survey3_grade6             = validated_data['survey3_grade6'],
            survey3_grade7             = validated_data['survey3_grade7'],
            survey3_grade8             = validated_data['survey3_grade8'],
            survey3_grade9             = validated_data['survey3_grade9'],
            survey3_grade10            = validated_data['survey3_grade10'],
            survey3_grade11            = validated_data['survey3_grade11'],
            survey1_feedback1          = validated_data['survey1_feedback1'],
            survey1_feedback2          = validated_data['survey1_feedback2'],
            survey1_feedback3          = validated_data['survey1_feedback3'],
            survey2_feedback1          = validated_data['survey2_feedback1'],
            survey2_feedback2          = validated_data['survey2_feedback2'],
            survey3_feedback1          = validated_data['survey3_feedback1'],
            survey3_feedback2          = validated_data['survey3_feedback2'],
            survey3_feedback3          = validated_data['survey3_feedback3'],
            survey3_feedback4          = validated_data['survey3_feedback4'],
            survey3_feedback5          = validated_data['survey3_feedback5'],
            survey3_feedback6          = validated_data['survey3_feedback6'],
            survey3_feedback7          = validated_data['survey3_feedback7'],
            survey3_feedback8          = validated_data['survey3_feedback8'],
            survey3_feedback9          = validated_data['survey3_feedback9'],
            survey3_feedback10         = validated_data['survey3_feedback10'],
            survey3_feedback11         = validated_data['survey3_feedback11']
        )

        evaluation.save()
        return evaluation
    class Meta:
        model  = Evaluation
        fields = '__all__'


class TraningMemoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        trainingmemmo = TrainingMemo.objects.create(
            date                       = validated_data['date'],
            dear                       = validated_data['dear'],
            to1                        = validated_data['to1'],
            to2                        = validated_data['to2'],
            volume_objective           = validated_data['volume_objective'],
            volume_actual              = validated_data['volume_actual'],
            volume_percent             = validated_data['volume_percent'],
            callproductivity_objective = validated_data['callproductivity_objective'],
            callproductivity_actual    = validated_data['callproductivity_actual'],
            callproductivity_percent   = validated_data['callproductivity_percent'],
            distribution_objective     = validated_data['distribution_objective'],
            distribution_actual        = validated_data['distribution_actual'],
            distribution_percent       = validated_data['distribution_percent'],
            range_objective            = validated_data['range_objective'],
            range_actual               = validated_data['range_actual'],
            range_percent              = validated_data['range_percent'],
            merchandising_objective    = validated_data['merchandising_objective'],
            merchandising_actual       = validated_data['merchandising_actual'],
            merchandising_percent      = validated_data['merchandising_percent'],
            cycle_objective            = validated_data['cycle_objective'],
            cycle_actual               = validated_data['cycle_actual'],
            cycle_percent              = validated_data['cycle_percent'],
            strength                   = validated_data['strength'],
            oppurtunities              = validated_data['oppurtunities'],
            insights                   = validated_data['insights'],
            actionplan                 = validated_data['actionplan'],
            nextstep                   = validated_data['nextstep']
        )

        trainingmemmo.save()
        return trainingmemmo

    class Meta:
        model  = TrainingMemo
        fields = '__all__'
