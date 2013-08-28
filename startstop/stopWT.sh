#!/bin/bash
echo Stopping the Oracle WebTier
echo $ORACLE_INSTANCE
${MW_HOME}/Oracle_WT1/opmn/bin/opmnctl stopall

