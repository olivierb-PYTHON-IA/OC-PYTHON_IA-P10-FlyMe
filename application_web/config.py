#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    #WEB APP CONFIGURATION
    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword")
    
    #LUIS APP CONFIGURATION
    LUIS_APP_ID = os.environ.get("LuisAppId")
    LUIS_API_KEY = os.environ.get("LuisAPIKey")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName")
    LUIS_API_ENDPOINT = os.environ.get("LuisAPIEndPoint")
    
    #APP INSIGHTS CONFIGURATION 
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey")
