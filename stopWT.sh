#!/bin/bash
echo Stopping the Oracle WebTier
echo $ORACLE_INSTANCE
${ORACLE_INSTANCE}/bin/opmnctl stopall

