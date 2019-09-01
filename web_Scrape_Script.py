# import
import re
import requests
from bs4 import BeautifulSoup as soup
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

html_string = """""


                    

                    
                    
                    
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">





<head>
<!--[if lt IE 9]><meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8"  /><![endif]-->
<!--[if gte IE 9]><meta http-equiv="X-UA-Compatible" content="IE=edge"> <![endif]-->	
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" href="/etc/designs/census/bootstrap.css" type="text/css"/>

	<link rel="stylesheet" href="/etc/designs/census/jquery.css" type="text/css"/>

	<link rel="stylesheet" href="/etc/designs/census/clientlibs.css" type="text/css"/>

    <link rel="stylesheet" href="/etc.clientlibs/census-core/clientlibs.css" type="text/css"/>

	
	    	  <link rel="icon" sizes="192x192" href="/etc/designs/census/images/icons/android-chrome-192x192.png">
    <link rel="icon" sizes="256x256" href="/etc/designs/census/images/icons/android-chrome-256x256.png">
     <link rel="shortcut icon" sizes="32x32" href="/etc/designs/census/images/icons/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/etc/designs/census/images/icons/apple-touch-icon-180x180.png">     
    <meta name="msapplication-square150x150logo" content="/etc/designs/census/images/icons/mstile-150x150.png"> 
	
		<title>Population and Housing Unit Estimates</title>
		<style type="text/css">
			.content_area{
				display:block;
			}
		</style>
	
	
			<link href="/etc/designs/census/clientlibs/css/print.css" rel="stylesheet" type="text/css" media="print"/>
	
	






                   
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="DC.title" property="og:title" content="Population and Housing Unit Estimates" />
<meta name="DC.creator" content="US Census Bureau" />
<meta name="DC.date.created" property="article:published_time" scheme="ISO8601" content="" />
<meta name="DC.date.reviewed" property="article:modified_time" scheme="ISO8601" content="2018-11-30T11:57:05.764-05:00" />
<meta name="DC.language" scheme="DCTERMS.RFC1766" content="EN-US" />
<meta name="robots" content="noodp, noydir" />
<meta name="author" content="US Census Bureau"  />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <meta http-equiv="keywords" content="" />
    <meta http-equiv="description" property="og:description" content="Produces estimates of the population for the United States, its states, counties, cities, and towns, as well as for the Commonwealth of Puerto Rico." />
      <meta property="og:locale" content="en_US" />
    <meta property="og:url" content="https://www.census.gov/popest" />

<meta property="og:image" content="https://www.census.gov/programs-surveys/popest.img.png/1528291005765.png" />


    <!-- context hub -->
 
<!-- DTM-->









<script type="text/javascript">
  
  var digitalData = digitalData || {};
    digitalData = {
        "page" : {
            "pageInfo" : {                
                "pageName" : "Population and Housing Unit Estimates_114724",
                "legacyPageName" : "en>programsRSUY>Population and Housing Unit Estimates",
                "pageURL" : window.location.href,
                "language" : "en",
                "pageTemplate" : "LPL",
                "tool" : "aem",
                "siteSection" : "programs-surveys","subSectionOne" : "popest"
            },
            "pageTag" : {
                "program" : "Program Survey Landing Page","program" : "Program Survey Landing Page|Population Estimates","collectionYear" : "2018","collectionYear" : "2018|2017"
            }
        },
        "event" : {
          "eventName" : {},
          "eventInfo" : {
            "share" : {},
            "download" : {},
            "search" : {},
            "expandCollapseList" : {},
            "language" : {},
            "landingPageTab" : {},
            "faceted" : {}
          }
        }
    };

    if ( typeof(Storage) !== "undefined" ) {
      if ( localStorage.getItem("pageLanguage") != null ) {
        digitalData.event.eventInfo.language.pageLanguage = localStorage.getItem("pageLanguage");
      }
      if ( localStorage.getItem("langEventName") != null ) {
        digitalData.event.eventName = localStorage.getItem("langEventName");
      }
      if ( localStorage.getItem("clickValue") != null ) {
        digitalData.event.eventInfo.search.clickValue = localStorage.getItem("clickValue");
      }
      if ( localStorage.getItem("searchEventName") != null ) {
        digitalData.event.eventName = localStorage.getItem("searchEventName");
      }
      /*if ( localStorage.getItem("landingPageTabClickValue") != null ) {
        digitalData.event.eventInfo.landingPageTab.clickValue = localStorage.getItem("landingPageTabClickValue");
      }*/ 
      if ( localStorage.getItem("tabEventName") != null ) {
        digitalData.event.eventName = localStorage.getItem("tabEventName");
      } 
      if ( localStorage.getItem("pageName") != null ) {
        digitalData.page.pageInfo.pageName = localStorage.getItem("pageName");
      }       
      //After assigning the value to digitalData, clear the localStorage variable's content
      localStorage.removeItem("pageLanguage");
      localStorage.removeItem("langEventName");
      localStorage.removeItem("clickValue");
      localStorage.removeItem("searchEventName");
      localStorage.removeItem("landingPageTabClickValue");
      localStorage.removeItem("tabEventName");
      localStorage.removeItem("pageName");
    } else {
      if ( getCookie("pageLanguage") != "" ) {
        digitalData.event.eventInfo.language.pageLanguage = getCookie("pageLanguage");
      }
      if ( getCookie("langEventName") != "" ) {
        digitalData.event.eventName = getCookie("langEventName");
      }
      if ( getCookie("clickValue") != "" ) {
        digitalData.event.eventInfo.search.clickValue = getCookie("clickValue");
      }
      if ( getCookie("searchEventName") != "" ) {
        digitalData.event.eventName = getCookie("searchEventName");
      }
      if ( getCookie("landingPageTabClickValue") != "" ) {
        digitalData.event.eventInfo.landingPageTab.clickValue = getCookie("landingPageTabClickValue");
      }
      if ( getCookie("tabEventName") != "" ) {
        digitalData.event.eventName = getCookie("tabEventName");
      }
      if ( getCookie("pageName") != "" ) {
        digitalData.page.pageInfo.pageName = getCookie("pageName");
      }
      //After assigning the value to digitalData, clear the localStorage variable's content
      setCookie("pageLanguage", "");
      setCookie("langEventName", "");
      setCookie("clickValue", "");
      setCookie("searchEventName", "");
      setCookie("landingPageTabClickValue", "");
      setCookie("pageName", "");
    }

    function setCookie(cname, cvalue, exdays) {
       var d = new Date();
       d.setTime(d.getTime() + (exdays*24*60*60*1000));
       var expires = "expires="+d.toUTCString();
       document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    function getCookie(cname) {
       var name = cname + "=";
       var ca = document.cookie.split(';');
       for(var i = 0; i < ca.length; i++) {
           var c = ca[i];
           while (c.charAt(0) == ' ') {
               c = c.substring(1);
           }
           if (c.indexOf(name) == 0) {
               return c.substring(name.length, c.length);
           }
       }
       return "";
    }

</script>

<script src="//assets.adobedtm.com/526d5084b7f8f688ea81a3aba09755d76a81f8e8/satelliteLib-5b0c69cba9998404374755048324ea6deb6c9db5.js"></script>

	
	

	<script type="text/javascript" src="https://www.google.com/jsapi"></script>
	
	
	<link rel="stylesheet" href="/etc/designs/census/censusfonts.css" type="text/css"/>

	<link rel="stylesheet" href="/etc/designs/census/orionicons.css" type="text/css"/>

	
	
	
	
		
			
<script>bazadebezolkohpepadr="1003747585"</script><script type="text/javascript" src="https://www.census.gov/akam/11/3bd3fa44" defer></script></head>



 
  
			  
<body id="innerPage" class="   ">
<div>
<div class="clientcontext parbase"><script type="text/javascript" src="/etc.clientlibs/clientlibs/granite/jquery.js"></script>
<script type="text/javascript" src="/etc.clientlibs/clientlibs/granite/utils.js"></script>
<script type="text/javascript" src="/etc.clientlibs/clientlibs/granite/jquery/granite.js"></script>
<script type="text/javascript" src="/etc.clientlibs/foundation/clientlibs/jquery.js"></script>
<script type="text/javascript" src="/etc.clientlibs/foundation/clientlibs/shared.js"></script>
<script type="text/javascript" src="/etc.clientlibs/clientlibs/granite/lodash/modern.js"></script>
<script type="text/javascript" src="/etc.clientlibs/cq/personalization/clientlib/personalization/kernel.js"></script>
<script type="text/javascript">
    $CQ(function() {
        CQ_Analytics.SegmentMgr.loadSegments("\/etc\/segmentation");
        CQ_Analytics.ClientContextUtils.init("\/etc\/clientcontext\/default", "\/content\/census\/en\/programs\u002Dsurveys\/popest");

        
    });
</script>
</div>

</div>
  
	
	<a name="skipfooter" class="skip"></a>
	
	<div class="uscb-main-container">
    	
			<div class="censusheader universalheader">

<header id="data-uscb-main-header" class="uscb-header uscb-print-hide">
	<a class="uscb-header-nav-skip uscb-button-medium uscb-secondary-button uscb-position-absolute" href="#content" tabindex="1">Skip to content</a>

    <div class="uscb-header-content">
        <div class="uscb-header-top uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center" onmouseover='CensusUniversalHeader.closeDropdowns("data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 7)'>
            <div class="uscb-menu-icon-container uscb-hide-gt-md" onclick='CensusUniversalHeader.toggleMenu("data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 0, 7)'>
                <div>
                    <div class="uscb-menu-bar1"></div>
                    <div class="uscb-menu-bar2"></div>
                    <div class="uscb-menu-bar3"></div>
                </div>
                <p id="data-uscb-header-close" class="uscb-header-close uscb-sub-heading-2 uscb-color-white uscb-bold" style="display: none;">CLOSE</p>
            </div>
            
            <div class="uscb-header-logo uscb-flex-row-gt-md-25 uscb-layout-align-gt-md-start-center uscb-flex-col-md-60 uscb-layout-align-md-center-center">            	
                <a href="https://www.census.gov/en.html" tabindex="0" onfocus="CensusSearchTypeahead.onSearchFocusBlur(false);">
                	<img class="uscb-nav-image" src="/etc/designs/census/images/USCENSUS_IDENTITY_SOLO_White_2in_TM.svg" alt="United States Census Bureau" title="U.S. Census Bureau"/>
               	</a>               	
            </div>
            
            
            
            
            
            
	            <hr class="uscb-header-footer-hr uscb-hide-gt-md"/>
	            <hr class="uscb-header-vert-hr uscb-hide-md"/>
	            <div class="uscb-header-search uscb-layout-row uscb-flex-row-gt-md-75 uscb-flex-col-md-40 uscb-layout-align-center-center">
	            	
	            	
	                
	                	
						
	<div class="uscb-header-backdrop" style="display: none;" onclick="CensusSearchTypeahead.onSearchFocusBlur(false)"></div>
	
	<i class="uscb-header-search-icon o-search-1" aria-hidden="true"></i>
	
	<form id="data-uscb-header-search-form" class="uscb-header-search-input-container uscb-layout-row uscb-layout-align-center-center" accept-charset="utf-8" action="https://www.census.gov/search-results.html?searchType=web&cssp=SERP&q=" method="GET">
	    <input type="text" id="data-uscb-header-input" name="q" class="uscb-header-input" placeholder="Search" aria-label="Search" onfocus="CensusSearchTypeahead.onSearchFocusBlur(true)" autocomplete="off"/>
	    	
		<input type="hidden" name="page" value="1"/> 
		<input type="hidden" name="stateGeo" value="none"/> 
		<input type="hidden" name="searchtype" value="web"/> 
		<input type="hidden" name="cssp" value="SERP"/>
		<input type="hidden" name="_charset_" value="UTF-8"/>
		
	    <button type="button" class="data-uscb-header-search-input-button uscb-header-search-input-button-close uscb-transparent-button o-close-1" style="display: none;" aria-label="Clear" onclick="CensusSearchTypeahead.onSearchCloseClick()">
	    </button>
	    <button type="button" class="data-uscb-header-search-input-button uscb-header-search-input-button-search uscb-primary-button" style="display: none;" onclick="CensusSearchTypeahead.onSearchButtonClick()">
	    	Search
	    </button>
	</form>
	
	<div id="data-uscb-header-search-typeahead" class="uscb-header-search-typeahead" style="display: none;">	    
                
	</div>

	<script type="text/javascript"> 
    	<!--/* Native onReady */-->  
		document.addEventListener("DOMContentLoaded", function(event) { 
			CensusSearchTypeahead.initSearchTypeahead("https://www.census.gov/suggest?operationName=httpsearch&query=", "https://www.census.gov/search-results.html?searchType=web&cssp=SERP&q=");
		});
	</script>

					
	            </div>
            
            
            
            
        </div>
        
        
	        <hr class="uscb-header-footer-hr uscb-hide-md"/>	        	        
        
       		
            <div class="uscb-layout-row">
            	<div class="uscb-header-nav-item-spacer-L" onmouseover='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 0, 7)'></div>
				
				<div class="uscb-header-menu uscb-layout-row uscb-w-100 uscb-hide-md">
					
						<div id="data-uscb-header-nav-item-0" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 0, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-0" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 0, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 0)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									Browse by Topic
								</div>
							</a>
							
							
						</div>
					
						<div id="data-uscb-header-nav-item-1" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 1, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-1" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 1, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 1)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									Explore Data
								</div>
							</a>
							
							
						</div>
					
						<div id="data-uscb-header-nav-item-2" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 2, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-2" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 2, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 2)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									Library
								</div>
							</a>
							
							
						</div>
					
						<div id="data-uscb-header-nav-item-3" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 3, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-3" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 3, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 3)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									Surveys/ Programs
								</div>
							</a>
							
							
						</div>
					
						<div id="data-uscb-header-nav-item-4" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 4, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-4" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 4, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 4)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									Information for…
								</div>
							</a>
							
							
						</div>
					
						<div id="data-uscb-header-nav-item-5" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 5, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-5" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 5, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 5)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									Find a Code
								</div>
							</a>
							
							
						</div>
					
						<div id="data-uscb-header-nav-item-6" class="uscb-header-nav-item uscb-height-100 uscb-padding-LR-8" style="display: flex; flex-basis: 14.285714285714286%; max-width: 183px" onmouseover='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 6, 7)'>
							
							
							<a id="data-uscb-header-nav-item-link-6" class="uscb-hw-100 uscb-text-align-center" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu(true, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 6, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-", 6)'>
								<div class="uscb-layout-row uscb-layout-align-center-center uscb-hw-100">
									About Us
								</div>
							</a>
							
							
						</div>
					

					<div class="uscb-flex" onmouseover='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 0, 7)'></div>
				</div>
				
				<div class="uscb-header-nav-item-spacer-R" onmouseover='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 0, 7)'></div>
            </div>
       		
       			        
       		
       		
				

					

					<div id="data-uscb-header-dropdown-links-0" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15 uscb-padding-LR-40 uscb-hide-md" style="
							display: none; 
                            max-width: ;
							width: ;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 0, 7)'>

						

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/topics/population/age-and-sex.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Age and Sex
	            					</a>								
								
	            					<a href="https://www.census.gov/businessandeconomy" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Business and Economy
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/education.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Education
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/preparedness.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Emergency Preparedness
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/employment.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Employment
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/topics/families.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Families and Living Arrangements
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/population/migration.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Geographic Mobility / Migration
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/geography.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Geography
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/health.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Health
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/population/hispanic-origin.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Hispanic Origin
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/topics/housing.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Housing
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/income-poverty.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Income and Poverty
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/international-trade.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						International Trade
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/population.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Population
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/population/population-estimates.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Population Estimates
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/topics/public-sector.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Public Sector
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/population/race.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Race
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/research.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Research
	            					</a>								
								
	            					<a href="https://www.census.gov/topics/public-sector/voting.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Voting and Registration
	            					</a>								
								
	            					<a href="https://www.census.gov/about/index.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" onkeydown="CensusUniversalHeader.onKeyChild(event, 'data-uscb-header-nav-item-link-0')" tabindex="-1">
	            						A - Z
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				

					

					<div id="data-uscb-header-dropdown-links-1" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15 uscb-padding-LR-40 uscb-hide-md" style="
							display: none; 
                            max-width: ;
							width: ;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 1, 7)'>

						

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/data.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Explore Data Main
	            					</a>								
								
	            					<a href="https://www.census.gov/academy" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Census Academy
	            					</a>								
								
	            					<a href="https://www.census.gov/about/what/admin-data.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Combining Data
	            					</a>								
								
	            					<a href="https://www.census.gov/data/data-tools.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Data Tools and Apps
	            					</a>								
								
	            					<a href="https://www.census.gov/developers/" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Developers
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/data/related-sites.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Related Sites
	            					</a>								
								
	            					<a href="https://www.census.gov/data/software.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Software
	            					</a>								
								
	            					<a href="https://www.census.gov/data/tables.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Tables
	            					</a>								
								
	            					<a href="https://www.census.gov/data/training-workshops.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Training and Workshops
	            					</a>								
								
	            					<a href="https://www.census.gov/library/visualizations.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" onkeydown="CensusUniversalHeader.onKeyChild(event, 'data-uscb-header-nav-item-link-1')" tabindex="-1">
	            						Visualizations
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				

					

					<div id="data-uscb-header-dropdown-links-2" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15 uscb-padding-LR-40 uscb-hide-md" style="
							display: none; 
                            max-width: ;
							width: ;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 2, 7)'>

						

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/library.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Library Main
	            					</a>								
								
	            					<a href="https://www.census.gov/AmericaCounts" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						America Counts: Stories
	            					</a>								
								
	            					<a href="https://www.census.gov/library/audio.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Audio
	            					</a>								
								
	            					<a href="https://www.census.gov/library/visualizations.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Infographics and Visualizations
	            					</a>								
								
	            					<a href="https://www.census.gov/library/photos.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Photos
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/library/publications.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Publications
	            					</a>								
								
	            					<a href="https://www.census.gov/library/video.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Videos
	            					</a>								
								
	            					<a href="https://www.census.gov/library/working-papers.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" onkeydown="CensusUniversalHeader.onKeyChild(event, 'data-uscb-header-nav-item-link-2')" tabindex="-1">
	            						Working Papers
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				

					

					<div id="data-uscb-header-dropdown-links-3" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15 uscb-padding-LR-40 uscb-hide-md" style="
							display: none; 
                            max-width: ;
							width: ;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 3, 7)'>

						

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/programs-surveys.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Surveys/Programs Main
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/are-you-in-a-survey.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Help for Survey Participants
	            					</a>								
								
	            					<a href="https://www.census.gov/2020census" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						2020 Census
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/decennial-census/decade/2010.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						2010 Census
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/acs" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						American Community Survey (ACS)
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/programs-surveys/ahs.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						American Housing Survey (AHS)
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/abs.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Annual Business Survey (ABS)
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/asm.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Annual Survey of Manufactures (ASM)
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/cog.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Census of Governments
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/cbp.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						County Business Patterns (CBP)
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/programs-surveys/cps.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Current Population Survey (CPS)
	            					</a>								
								
	            					<a href="https://www.census.gov/EconomicCensus" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Economic Census
	            					</a>								
								
	            					<a href="https://www.census.gov/internationalprograms" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						International Programs
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/metro-micro.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Metro and Micro Areas
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/popproj.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Population Projections
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/programs-surveys/saipe.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Small Area Income and Poverty
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/susb.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Statistics of U.S. Businesses
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/sbo.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Survey of Business Owners
	            					</a>								
								
	            					<a href="https://www.census.gov/sipp/" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Survey of Income and Program Participation (SIPP)
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/surveys-programs.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" onkeydown="CensusUniversalHeader.onKeyChild(event, 'data-uscb-header-nav-item-link-3')" tabindex="-1">
	            						All surveys and programs
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				

					

					<div id="data-uscb-header-dropdown-links-4" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15  uscb-hide-md" style="
							display: none; 
                            max-width: 183px;
							width: 14.285714285714286%;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 4, 7)'>

						<style>
                        	@media screen and (min-width: 1281px) {
                            	#data-uscb-header-dropdown-links-4 {
                                	left: 732px;
                                }
                            }
                            @media screen and (max-width: 1281px) {
                            	#data-uscb-header-dropdown-links-4 {
                                	left: 57.142857142857146%;
                                }
                            }
                        </style>

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 100%;">
								
								
								
								
	            					<a href="https://www.census.gov/newsroom.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Media (Newsroom)
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/are-you-in-a-survey.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Survey Participants/ Respondents
	            					</a>								
								
	            					<a href="https://www.census.gov/partners" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Partners
	            					</a>								
								
	            					<a href="https://www.census.gov/programs-surveys/sis.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" onkeydown="CensusUniversalHeader.onKeyChild(event, 'data-uscb-header-nav-item-link-4')" tabindex="-1">
	            						Educators and Students
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				

					

					<div id="data-uscb-header-dropdown-links-5" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15  uscb-hide-md" style="
							display: none; 
                            max-width: 183px;
							width: 14.285714285714286%;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 5, 7)'>

						<style>
                        	@media screen and (min-width: 1281px) {
                            	#data-uscb-header-dropdown-links-5 {
                                	left: 915px;
                                }
                            }
                            @media screen and (max-width: 1281px) {
                            	#data-uscb-header-dropdown-links-5 {
                                	left: 71.42857142857143%;
                                }
                            }
                        </style>

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 100%;">
								
								
								
								
	            					<a href="https://www.census.gov/library/reference/code-lists/naics.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						NAICS Lookup
	            					</a>								
								
	            					<a href="https://www.census.gov/library/reference/code-lists/schedule/b.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Schedule B Search
	            					</a>								
								
	            					<a href="https://www.census.gov/data/developers/data-sets/Geocoding-services.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" onkeydown="CensusUniversalHeader.onKeyChild(event, 'data-uscb-header-nav-item-link-5')" tabindex="-1">
	            						Geocoding Service
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				

					

					<div id="data-uscb-header-dropdown-links-6" class="uscb-header-dropdown-links uscb-layout-row uscb-padding-TB-10 uscb-padding-LR-15 uscb-padding-LR-40 uscb-hide-md" style="
							display: none; 
                            max-width: ;
							width: ;" onmouseleave='CensusUniversalHeader.onActivateMenu(false, "data-uscb-header-dropdown-links-", "data-uscb-header-nav-item-", "data-uscb-header-nav-item-link-", 6, 7)'>

						

						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/about-us" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						About the Bureau
	            					</a>								
								
	            					<a href="https://www.census.gov/about/who.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Who We Are
	            					</a>								
								
	            					<a href="https://www.census.gov/about/what.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						What We Do
	            					</a>								
								
	            					<a href="https://www.census.gov/about/business-opportunities.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Business Opportunities
	            					</a>								
								
	            					<a href="https://www.census.gov/careers" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Census Careers
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/fieldjobs" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Field Jobs by State
	            					</a>								
								
	            					<a href="https://www.census.gov/about/what/admin-data.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Combining Data
	            					</a>								
								
	            					<a href="https://www.census.gov/about/history.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Our History
	            					</a>								
								
	            					<a href="https://www.census.gov/about/policies.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Policies and Notices
	            					</a>								
								
	            					<a href="https://www.census.gov/privacy" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Privacy Program
	            					</a>								
																
							
							</div>
						
							<div class="uscb-layout-column uscb-flex-row uscb-padding-LR-0" style="flex-basis: 25%;">
								
								
								
								
	            					<a href="https://www.census.gov/regions" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Regional Offices 
	            					</a>								
								
	            					<a href="https://www.census.gov/about/contact-us/staff-finder.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Staff Directory
	            					</a>								
								
	            					<a href="https://www.census.gov/about/contact-us.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						Contact Us
	            					</a>								
								
	            					<a href="https://www.census.gov/about/faqs.html" class="data-uscb-header-dropdown-link-item uscb-header-dropdown-link-item uscb-padding-TB-10" tabindex="-1">
	            						FAQs
	            					</a>								
																
							
							</div>
						
						
					</div>
				
				
       		
        
        
        
        <div id="data-uscb-header-menu" class="uscb-header-menu uscb-layout-row uscb-hide-gt-md uscb-hide-md">
        
       		
            <div class="uscb-header-menu-top-level uscb-flex-row-33 uscb-layout-column">
            
            	
				
					<div id="data-uscb-header-nav-item-side-0" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 0, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 0)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">Browse by Topic</div>
		                </a>
		                
		                
		                
		            </div>
				
				
					<div id="data-uscb-header-nav-item-side-1" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 1, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 1)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">Explore Data</div>
		                </a>
		                
		                
		                
		            </div>
				
				
					<div id="data-uscb-header-nav-item-side-2" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 2, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 2)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">Library</div>
		                </a>
		                
		                
		                
		            </div>
				
				
					<div id="data-uscb-header-nav-item-side-3" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 3, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 3)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">Surveys/ Programs</div>
		                </a>
		                
		                
		                
		            </div>
				
				
					<div id="data-uscb-header-nav-item-side-4" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 4, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 4)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">Information for…</div>
		                </a>
		                
		                
		                
		            </div>
				
				
					<div id="data-uscb-header-nav-item-side-5" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 5, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 5)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">Find a Code</div>
		                </a>
		                
		                
		                
		            </div>
				
				
					<div id="data-uscb-header-nav-item-side-6" class="uscb-header-nav-item uscb-layout-column uscb-layout-align-center-center" style="display: flex; flex-basis: 14.285714285714286%;">
						
						
		                <a class="uscb-hw-100" tabindex="0" onfocus='CensusUniversalHeader.onActivateMenu("toggle", "data-uscb-header-dropdown-links-side-", "data-uscb-header-nav-item-side-", "data-uscb-header-nav-item-link-", 6, 7)' onkeydown='CensusUniversalHeader.onKeyParent(event, "data-uscb-header-dropdown-links-side-", 6)'>
		                    <div class="uscb-layout-row uscb-layout-align-start-center uscb-hw-100 uscb-padding-LR-10">About Us</div>
		                </a>
		                
		                
		                
		            </div>
				

				

            </div>            
       		
       		
       		
            <div class="uscb-header-menu-sub-level uscb-flex-row-67 uscb-layout-column">
            
	            
					
					<div id="data-uscb-header-dropdown-links-side-0" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/topics/population/age-and-sex.html" class="uscb-header-dropdown-link-item">
           						Age and Sex
           					</a>								
													
           					<a href="https://www.census.gov/businessandeconomy" class="uscb-header-dropdown-link-item">
           						Business and Economy
           					</a>								
													
           					<a href="https://www.census.gov/topics/education.html" class="uscb-header-dropdown-link-item">
           						Education
           					</a>								
													
           					<a href="https://www.census.gov/topics/preparedness.html" class="uscb-header-dropdown-link-item">
           						Emergency Preparedness
           					</a>								
													
           					<a href="https://www.census.gov/topics/employment.html" class="uscb-header-dropdown-link-item">
           						Employment
           					</a>								
													
           					<a href="https://www.census.gov/topics/families.html" class="uscb-header-dropdown-link-item">
           						Families and Living Arrangements
           					</a>								
													
           					<a href="https://www.census.gov/topics/population/migration.html" class="uscb-header-dropdown-link-item">
           						Geographic Mobility / Migration
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/geography.html" class="uscb-header-dropdown-link-item">
           						Geography
           					</a>								
													
           					<a href="https://www.census.gov/topics/health.html" class="uscb-header-dropdown-link-item">
           						Health
           					</a>								
													
           					<a href="https://www.census.gov/topics/population/hispanic-origin.html" class="uscb-header-dropdown-link-item">
           						Hispanic Origin
           					</a>								
													
           					<a href="https://www.census.gov/topics/housing.html" class="uscb-header-dropdown-link-item">
           						Housing
           					</a>								
													
           					<a href="https://www.census.gov/topics/income-poverty.html" class="uscb-header-dropdown-link-item">
           						Income and Poverty
           					</a>								
													
           					<a href="https://www.census.gov/topics/international-trade.html" class="uscb-header-dropdown-link-item">
           						International Trade
           					</a>								
													
           					<a href="https://www.census.gov/topics/population.html" class="uscb-header-dropdown-link-item">
           						Population
           					</a>								
													
           					<a href="https://www.census.gov/topics/population/population-estimates.html" class="uscb-header-dropdown-link-item">
           						Population Estimates
           					</a>								
													
           					<a href="https://www.census.gov/topics/public-sector.html" class="uscb-header-dropdown-link-item">
           						Public Sector
           					</a>								
													
           					<a href="https://www.census.gov/topics/population/race.html" class="uscb-header-dropdown-link-item">
           						Race
           					</a>								
													
           					<a href="https://www.census.gov/topics/research.html" class="uscb-header-dropdown-link-item">
           						Research
           					</a>								
													
           					<a href="https://www.census.gov/topics/public-sector/voting.html" class="uscb-header-dropdown-link-item">
           						Voting and Registration
           					</a>								
													
           					<a href="https://www.census.gov/about/index.html" class="uscb-header-dropdown-link-item">
           						A - Z
           					</a>								
							
						
					</div>
					
				
					
					<div id="data-uscb-header-dropdown-links-side-1" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/data.html" class="uscb-header-dropdown-link-item">
           						Explore Data Main
           					</a>								
													
           					<a href="https://www.census.gov/academy" class="uscb-header-dropdown-link-item">
           						Census Academy
           					</a>								
													
           					<a href="https://www.census.gov/about/what/admin-data.html" class="uscb-header-dropdown-link-item">
           						Combining Data
           					</a>								
													
           					<a href="https://www.census.gov/data/data-tools.html" class="uscb-header-dropdown-link-item">
           						Data Tools and Apps
           					</a>								
													
           					<a href="https://www.census.gov/developers/" class="uscb-header-dropdown-link-item">
           						Developers
           					</a>								
													
           					<a href="https://www.census.gov/data/related-sites.html" class="uscb-header-dropdown-link-item">
           						Related Sites
           					</a>								
													
           					<a href="https://www.census.gov/data/software.html" class="uscb-header-dropdown-link-item">
           						Software
           					</a>								
													
           					<a href="https://www.census.gov/data/tables.html" class="uscb-header-dropdown-link-item">
           						Tables
           					</a>								
													
           					<a href="https://www.census.gov/data/training-workshops.html" class="uscb-header-dropdown-link-item">
           						Training and Workshops
           					</a>								
													
           					<a href="https://www.census.gov/library/visualizations.html" class="uscb-header-dropdown-link-item">
           						Visualizations
           					</a>								
							
						
					</div>
					
				
					
					<div id="data-uscb-header-dropdown-links-side-2" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/library.html" class="uscb-header-dropdown-link-item">
           						Library Main
           					</a>								
													
           					<a href="https://www.census.gov/AmericaCounts" class="uscb-header-dropdown-link-item">
           						America Counts: Stories
           					</a>								
													
           					<a href="https://www.census.gov/library/audio.html" class="uscb-header-dropdown-link-item">
           						Audio
           					</a>								
													
           					<a href="https://www.census.gov/library/visualizations.html" class="uscb-header-dropdown-link-item">
           						Infographics and Visualizations
           					</a>								
													
           					<a href="https://www.census.gov/library/photos.html" class="uscb-header-dropdown-link-item">
           						Photos
           					</a>								
													
           					<a href="https://www.census.gov/library/publications.html" class="uscb-header-dropdown-link-item">
           						Publications
           					</a>								
													
           					<a href="https://www.census.gov/library/video.html" class="uscb-header-dropdown-link-item">
           						Videos
           					</a>								
													
           					<a href="https://www.census.gov/library/working-papers.html" class="uscb-header-dropdown-link-item">
           						Working Papers
           					</a>								
							
						
					</div>
					
				
					
					<div id="data-uscb-header-dropdown-links-side-3" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/programs-surveys.html" class="uscb-header-dropdown-link-item">
           						Surveys/Programs Main
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/are-you-in-a-survey.html" class="uscb-header-dropdown-link-item">
           						Help for Survey Participants
           					</a>								
													
           					<a href="https://www.census.gov/2020census" class="uscb-header-dropdown-link-item">
           						2020 Census
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/decennial-census/decade/2010.html" class="uscb-header-dropdown-link-item">
           						2010 Census
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/acs" class="uscb-header-dropdown-link-item">
           						American Community Survey (ACS)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/ahs.html" class="uscb-header-dropdown-link-item">
           						American Housing Survey (AHS)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/abs.html" class="uscb-header-dropdown-link-item">
           						Annual Business Survey (ABS)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/asm.html" class="uscb-header-dropdown-link-item">
           						Annual Survey of Manufactures (ASM)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/cog.html" class="uscb-header-dropdown-link-item">
           						Census of Governments
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/cbp.html" class="uscb-header-dropdown-link-item">
           						County Business Patterns (CBP)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/cps.html" class="uscb-header-dropdown-link-item">
           						Current Population Survey (CPS)
           					</a>								
													
           					<a href="https://www.census.gov/EconomicCensus" class="uscb-header-dropdown-link-item">
           						Economic Census
           					</a>								
													
           					<a href="https://www.census.gov/internationalprograms" class="uscb-header-dropdown-link-item">
           						International Programs
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/metro-micro.html" class="uscb-header-dropdown-link-item">
           						Metro and Micro Areas
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/popproj.html" class="uscb-header-dropdown-link-item">
           						Population Projections
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/saipe.html" class="uscb-header-dropdown-link-item">
           						Small Area Income and Poverty
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/susb.html" class="uscb-header-dropdown-link-item">
           						Statistics of U.S. Businesses
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/sbo.html" class="uscb-header-dropdown-link-item">
           						Survey of Business Owners
           					</a>								
													
           					<a href="https://www.census.gov/sipp/" class="uscb-header-dropdown-link-item">
           						Survey of Income and Program Participation (SIPP)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/surveys-programs.html" class="uscb-header-dropdown-link-item">
           						All surveys and programs
           					</a>								
							
						
					</div>
					
				
					
					<div id="data-uscb-header-dropdown-links-side-4" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/newsroom.html" class="uscb-header-dropdown-link-item">
           						Media (Newsroom)
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/are-you-in-a-survey.html" class="uscb-header-dropdown-link-item">
           						Survey Participants/ Respondents
           					</a>								
													
           					<a href="https://www.census.gov/partners" class="uscb-header-dropdown-link-item">
           						Partners
           					</a>								
													
           					<a href="https://www.census.gov/programs-surveys/sis.html" class="uscb-header-dropdown-link-item">
           						Educators and Students
           					</a>								
							
						
					</div>
					
				
					
					<div id="data-uscb-header-dropdown-links-side-5" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/library/reference/code-lists/naics.html" class="uscb-header-dropdown-link-item">
           						NAICS Lookup
           					</a>								
													
           					<a href="https://www.census.gov/library/reference/code-lists/schedule/b.html" class="uscb-header-dropdown-link-item">
           						Schedule B Search
           					</a>								
													
           					<a href="https://www.census.gov/data/developers/data-sets/Geocoding-services.html" class="uscb-header-dropdown-link-item">
           						Geocoding Service
           					</a>								
							
						
					</div>
					
				
					
					<div id="data-uscb-header-dropdown-links-side-6" class="uscb-header-dropdown-links uscb-layout-column" style="height: 40px; display: none;">
						
													
           					<a href="https://www.census.gov/about-us" class="uscb-header-dropdown-link-item">
           						About the Bureau
           					</a>								
													
           					<a href="https://www.census.gov/about/who.html" class="uscb-header-dropdown-link-item">
           						Who We Are
           					</a>								
													
           					<a href="https://www.census.gov/about/what.html" class="uscb-header-dropdown-link-item">
           						What We Do
           					</a>								
													
           					<a href="https://www.census.gov/about/business-opportunities.html" class="uscb-header-dropdown-link-item">
           						Business Opportunities
           					</a>								
													
           					<a href="https://www.census.gov/careers" class="uscb-header-dropdown-link-item">
           						Census Careers
           					</a>								
													
           					<a href="https://www.census.gov/fieldjobs" class="uscb-header-dropdown-link-item">
           						Field Jobs by State
           					</a>								
													
           					<a href="https://www.census.gov/about/what/admin-data.html" class="uscb-header-dropdown-link-item">
           						Combining Data
           					</a>								
													
           					<a href="https://www.census.gov/about/history.html" class="uscb-header-dropdown-link-item">
           						Our History
           					</a>								
													
           					<a href="https://www.census.gov/about/policies.html" class="uscb-header-dropdown-link-item">
           						Policies and Notices
           					</a>								
													
           					<a href="https://www.census.gov/privacy" class="uscb-header-dropdown-link-item">
           						Privacy Program
           					</a>								
													
           					<a href="https://www.census.gov/regions" class="uscb-header-dropdown-link-item">
           						Regional Offices 
           					</a>								
													
           					<a href="https://www.census.gov/about/contact-us/staff-finder.html" class="uscb-header-dropdown-link-item">
           						Staff Directory
           					</a>								
													
           					<a href="https://www.census.gov/about/contact-us.html" class="uscb-header-dropdown-link-item">
           						Contact Us
           					</a>								
													
           					<a href="https://www.census.gov/about/faqs.html" class="uscb-header-dropdown-link-item">
           						FAQs
           					</a>								
							
						
					</div>
					
				 
				              
            </div>
       		
       		
        </div>
        
    </div>
</header>

<script type="text/javascript">
	document.addEventListener("DOMContentLoaded", function(event) { 
		CensusUniversalHeader.initHeader();
	});
</script></div>

		
	</div>
	<div class="container-fluid">
		<div class="topBg"></div>
			
		<div class="wrapper wrapperMarginTop">
		
			







<a name="skip"> </a>
<div id="sectionTitleRow" class="belowHeader row no-gutter">
		<div class="col-xs-12 uscb-margin-T-5">
		<div id="breadContainer" class="belowHeader hidden-xs visible-lg uscb-print-hide">	
	<ul class="uscb-layout-row uscb-top-pagination uscb-layout-align-start-center">
		
            <li>
                
                    <a tabindex="0" href="/en.html" class="uscb-top-pagination-links" onclick="CQ_Analytics.record({event:'followBreadcrumb',values: { breadcrumbPath: '/content/census/en.html' },collect: false,options: { obj: this }})">
                            Census.gov
                    </a>
                    <span>></span>
                			
                
            </li>
		
            <li>
                
                    <a tabindex="0" href="/programs-surveys.html" class="uscb-top-pagination-links" onclick="CQ_Analytics.record({event:'followBreadcrumb',values: { breadcrumbPath: '/content/census/en/programs-surveys.html' },collect: false,options: { obj: this }})">
                            Our Surveys &amp; Programs
                    </a>
                    <span>></span>
                			
                
            </li>
		
            <li>
                			
                <span class="uscb-top-pagination-links">Population and Housing Unit Estimates</span>
            </li>
		
	</ul>
</div>
	</div>
	
	<div id="infoBannerSection" class="col-xs-12 uscb-padding-LR-0">
		



	
	


<script type="text/javascript">	
	function getBanners() {		
		var urlVal = "\/content\/census\/en\/programs\u002Dsurveys\/popest.infobanners.html";
			$.ajax({
			url: urlVal,		dataType: "html",	
			success: function( result ) {
				$('infoBannerSection').html(result);

			},
			error: function( err ){
  				console.log(err);
			}
		});		

		return false;
	}
	$(document).ready(function(){
        getBanners();
		$('.info-banner-clickable-div').click(function(e) {			
		    var href = $(this).attr('id');	    
		    if( typeof(href) !== 'undefined' && !$(e.target).hasClass('data-uscb-exit-btn') && !$(e.target).hasClass('data-uscb-banner-dismiss-btn') ){
		    	window.location = href;
		    }
		    return false;
		});

		$('.uscb-banner-pointer-div').hover(
			function(e) {
				$hoverTargets = $(this).find(".data-uscb-banner-hover-target");
				$hoverTargets.addClass("uscb-text-decoration-underline");
				$hoverTargets.removeClass("uscb-text-decoration-none");
			},
			function(e) {
				$hoverTargets = $(this).find(".data-uscb-banner-hover-target");
				$hoverTargets.removeClass("uscb-text-decoration-underline");
				$hoverTargets.addClass("uscb-text-decoration-none");
			}
		);

		$('.data-uscb-banner-dismiss-btn').click(function(e){
			if ( $(e.target).hasClass('data-uscb-banner-dismiss-btn') ) {
				var dismissedBannerClass = $(this).attr('id');
				var randStr = $(this).attr('id');
				var existingCookieValue = getCookie('dismissedBannersClasses');
		        var newValue = (typeof(existingCookieValue) != 'undefined' && existingCookieValue != '') ? existingCookieValue + '|' + dismissedBannerClass : dismissedBannerClass;

                setCookie('dismissedBannersClasses', newValue,7);
                $('.info-banner-section_' + randStr).remove();       
			}
		});

	});
</script> 




	</div>
	
	<div class="col-xs-9 col-lg-8">				
			     
	   	<span>	   	   
	    	        
            <h1 class="uscb-h1 uscb-medium">Population and Housing Unit Estimates</h1>   
       	</span> 
             
</div>
	
	
	
	
	<div class="hidden-xs hidden-sm hidden-md col-lg-4 uscb-padding-R-0">
		<div id="desktopLanguageSelectorContainer" class="pull-right">			
	   		
	

	
	
	


	   	</div>
	</div>
	
<script type="text/javascript">

	$(document).ready(function(){		
		$(document).click(function(event) {			
			if( $(event.target).is('#mobileFacetSelection') ) {
				closeMobileFacetSelection();
			}else{
				//span('clicked inside...');
			}		         
		});
	});//end document.ready function

	function toggleMobileLeftNavigation() {		
		if( $('.leftNavigation').hasClass('no-show') ) {			
			$('.leftNavigation').removeClass('no-show');
			$('.belowHeader:not(#sectionTitleRow, #listPageContent)').hide();
			$('#infoBannerSection').hide();
		}else{			
			$('.leftNavigation').addClass('no-show');			
			$('.belowHeader:not(#sectionTitleRow, #listPageContent)').show();
			$('#infoBannerSection').show();
		}		
		$('#sectionTitleRow .leftNavButton').toggleClass('open');
		$('#mobileTitleRow').toggleClass('menuHeader');
		$('#sectionTitleRow').toggleClass('menuHeader');
		var sectionTitleRowHeight = $('#sectionTitleRow').height();
		var leftNavPaddingOffset = 150;
		if (sectionTitleRowHeight)
			leftNavPaddingOffset = sectionTitleRowHeight + 65;

		$('#mobileLeftNavigation .menuContent').css('padding-top', sectionTitleRowHeight + 65 + 'px');
	}	
	
  	function toggleFacetSelection() {		
  		if( !$('body').hasClass('menu-slider') ){        	
        	$('body').addClass('menu-slider');
        	$('body').addClass('in');
        }else{        	
        	$('body').removeClass('menu-slider');
        	$('body').removeClass('in');
        }
  	}
  	
  	function openMobileFacetSelection() {
  		$('#mobileFacetSelection').css('width', '100%');  		
  	}
  	
  	function closeMobileFacetSelection() {  		
  		$('#mobileFacetSelection').css('width', '0%');
  	}
  	
</script>	
</div>

<div class="row no-gutter">
	
	<div id="leftColumn" class="col-lg-2">
		
			<div class="grid_navInnerLandingHolder">
				



<a href="#skipsideNav" class="offscreen">Skip to looking for section</a>
	<div class="grid_navInnerLandingLinks">
		<!-- begin Navigation items -->
		
				<div class="leftnav">




	<div>
  

  

  
	  
	  
	  
		  
	  
		  
	  
		  
	  
		  
	  
		  
	  
		  
	  
		  
	  
	  
  
	  
	  
	  
		  
	  
		  
	  
		  
	  
		  
	  
		  
	  
	  
  
	  
	  
	  
		  
	  
		  
	  
	  
  
	  
	  
	  
	  
  
	  
	  
	  
		  
	  
		  
	  
	  
  
	  
	  
	  
		  
	  
		  
	  
		  
	  
	  
  
	  
	  
	  
	  
  
	  
	  
	  
		  
	  
		  
	  
		  
	  
	  
  

  <ul class="uscb-filter-list uscb-margin-L--10 uscb-print-hide visible-lg uscb-print-hide">
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/about.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>About this Section</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/data.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>Data</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/geographies.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>Geographies</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/guidance.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>Guidance for Data Users</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/guidance-geographies.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>Guidance for Geographies Users</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/library.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>Library</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/news.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>News</span>
			  </a>
		  </span>
	  </li>
  
	  
	  <li class="uscb-filter-parent">
		  
		  <span>
			  <a href="/programs-surveys/popest/technical-documentation.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
				  <span>Technical Documentation</span>
			  </a>
		  </span>
	  </li>
  </ul>

  <div class="visible-lg uscb-print-hide">
	  <div class="uscb-layout-row uscb-margin-T-10">
		  <i class="o-angle-left-1 uscb-color-accent uscb-font-2x uscb-margin-R-10 uscb-position-relative" style="top: -8px"></i>
		  <a href="/programs-surveys.html" class="uscb-color-primary uscb-medium uscb-underline-hover">
			  <span>Back to Our Surveys &amp; Programs</span>
		  </a>
	  </div>
  </div>

  
  
  <div class="hidden-lg uscb-margin-B-8 uscb-print-hide">
	  <div class="ui-widget uscb-input-wrapper" id="data-uscb-input-wrapper-mobile-nav">
		  <div class="uscb-dropdown-container uscb-layout-row">
			  <input class="tags uscb-flex-row-gt-sm-90 uscb-flex-row-sm-8" placeholder="Sections" style="height: 34px;"/>
			  <div class="uscb-form-dropdown-button-chevron uscb-icon-button">
				  <i class="o-angle-down-1 uscb-font-2x uscb-color-accent" alt=""></i>
			  </div>
		  </div>

		  

		  
			  
			  
			  
				  
			  
				  
			  
				  
			  
				  
			  
				  
			  
				  
			  
				  
			  
			  
		  
			  
			  
			  
				  
			  
				  
			  
				  
			  
				  
			  
				  
			  
			  
		  
			  
			  
			  
				  
			  
				  
			  
			  
		  
			  
			  
			  
			  
		  
			  
			  
			  
				  
			  
				  
			  
			  
		  
			  
			  
			  
				  
			  
				  
			  
				  
			  
			  
		  
			  
			  
			  
			  
		  
			  
			  
			  
				  
			  
				  
			  
				  
			  
			  
		  

		  <ul class="uscb-filter-list uscb-w-100" style="float: left; display: none;">
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/about.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>About this Section</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/data.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>Data</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/geographies.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>Geographies</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/guidance.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>Guidance for Data Users</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/guidance-geographies.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>Guidance for Geographies Users</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/library.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>Library</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/news.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>News</span>
						  </a>
					  </span>
				  </li>
			  

				  
				  <li class="uscb-filter-parent uscb-border-0 uscb-padding-0">
					  
					  <span>
						  <a href="/programs-surveys/popest/technical-documentation.html" tabindex="0" class="uscb-color-primary" style="font-size: 1rem;">
							  <span>Technical Documentation</span>
						  </a>
					  </span>
				  </li>
			  
			  <div class="uscb-layout-row uscb-margin-T-10 uscb-margin-L-15 uscb-underline-hover" style="height: 27px;">
				  <i class="o-angle-left-1 uscb-color-accent uscb-font-2x uscb-margin-R-10 uscb-position-relative" style="top: -9px"></i>
				  <a href="/programs-surveys.html" class="uscb-color-primary uscb-h-100">
					  <span class="uscb-bold">Back to Our Surveys &amp; Programs</span>
				  </a>
			  </div>
		  </ul>
	  </div>

	  <div id="data-uscb-download-btn-wrapper-" class="uscb-layout-row uscb-layout-align-flex-end"></div>

	  <noscript>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">About this Section</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">Data</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">Geographies</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">Guidance for Data Users</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">Guidance for Geographies Users</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">Library</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">News</a>
				  </li>
			  </ul>
		  
			  <ul class="left geoList uscb-filter-list">
				  <li class="uscb-filter-parent">
					  <a tabindex="0">Technical Documentation</a>
				  </li>
			  </ul>
		  
	  </noscript>
  </div>
</div>




</div>

		  
	</div>

		<div class="sponsorlogo sponsoringlogo image"><div id="sponsorLogoHolder" class="uscb-print-hide">
  
  
</div>

</div>

	
			</div>
		
	</div>
	
	
	<a name="skipNav-CMSContent" id="skipNav-CMSContent"></a>
	<!--  Content -->
	
	 <div class="belowHeader col-lg-10" id="rightContent">
	
		<div class="row nested-row no-gutter">
			<div id="landingIntro">
				
<!-- <div style="grid_content_LandingSubContent">-->

<div class="row nested-row grid_content_landingTitle">
</div>
<div class="row nested-row">
	<div class="herotextimage"><div style="min-height: 75px;" class="grid_content_landingText"> 
	<div id="landingAboutText">
		
		<span class="uscb-body-text"><p>The Census Bureau's Population Estimates Program (PEP) produces estimates of the population for the United States, states, metropolitan and micropolitan statistical areas, counties, cities, towns, as well as for Puerto Rico and its municipios.</p>
</span>
	    <a href="/programs-surveys/popest/about.html" tabindex="0" title="This section provides detailed information and statistics on Population Estimates. Find the latest news, publications, and other content.>" class="uscb-padding-T-2 uscb-margin-B-10 uscb-float-left">
	    	Read More
	    </a>
	</div>  
	

    <div id="landingHeroMultimedia" class="hidden-xs hidden-sm visible-md visible-lg"> 
    	<img class="grid_content_landingImg" src="/content/census/en/programs-surveys/popest/_jcr_content/herotextimage.texthero.jpg/1521727618274.jpg" alt="Population Estimates" title="Population Estimates"/>
    </div>
           
	
</div></div>

	<!-- begin data table for subtopic data -->
	<div id="landingSubdata" style="display: inline-block;">
		<div class="subfeature landingsubfeature">
		
	<br/>
	<div class="selectedSubFeature"><div class="uscb-margin-T-10 uscb-layout-row uscb-layout-column-sm uscb-layout-align-space-between">
	
		<div class="uscb-width-gt-sm-33 uscb-text-align-center uscb-margin-TB-20">
			<a href="/programs-surveys/popest/data/tables.html" tabindex="0" target="_self"> 
				<span data-picture> 
					<span data-src='/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.1.png/1550167480226.png'></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.1.140.medium.png/1550167480226.png" data-media="(max-width: 576px)"></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.1.90.medium.png/1550167480226.png" data-media=" (min-width: 577px)"></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.1.140.medium.png/1550167480226.png" data-media=" (min-width: 801px)"></span>
					
					<noscript>
						<img src="https://www.census.gov/programs-surveys/popest/_jcr_content/featureicons.featureicon.1.png/1550167480226.png"/>
					</noscript>
				</span> 
				<div class="uscb-margin-T-sm-10 uscb-margin-T-gt-sm-30 uscb-margin-LR-16 uscb-sans-condensed uscb-font-lg uscb-line-height-24">Vintage 2018 Tables</div>
			</a>
		</div>
		<hr class="uscb-vertical-hr uscb-border-secondary-2 uscb-hide-1259" style="margin-top: 170px"/>
		<hr class="uscb-hr-flex     uscb-border-secondary-2 uscb-hide-gt-sm uscb-margin-TB-0"/>
	
		<div class="uscb-width-gt-sm-34 uscb-text-align-center uscb-margin-TB-20">
			<a href="/programs-surveys/popest/technical-documentation.html" tabindex="0" target="_self"> 
				<span data-picture> 
					<span data-src='/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.2.png/1550167478979.png'></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.2.140.medium.png/1550167478979.png" data-media="(max-width: 576px)"></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.2.90.medium.png/1550167478979.png" data-media=" (min-width: 577px)"></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.2.140.medium.png/1550167478979.png" data-media=" (min-width: 801px)"></span>
					
					<noscript>
						<img src="https://www.census.gov/programs-surveys/popest/_jcr_content/featureicons.featureicon.2.png/1550167478979.png"/>
					</noscript>
				</span> 
				<div class="uscb-margin-T-sm-10 uscb-margin-T-gt-sm-30 uscb-margin-LR-16 uscb-sans-condensed uscb-font-lg uscb-line-height-24">Technical Documentation</div>
			</a>
		</div>
		<hr class="uscb-vertical-hr uscb-border-secondary-2 uscb-hide-1259" style="margin-top: 170px"/>
		<hr class="uscb-hr-flex     uscb-border-secondary-2 uscb-hide-gt-sm uscb-margin-TB-0"/>
	
		<div class="uscb-width-gt-sm-33 uscb-text-align-center uscb-margin-TB-20">
			<a href="/programs-surveys/popest/about/schedule.html" tabindex="0" target="_self"> 
				<span data-picture> 
					<span data-src='/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.3.png/1550167479521.png'></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.3.140.medium.png/1550167479521.png" data-media="(max-width: 576px)"></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.3.90.medium.png/1550167479521.png" data-media=" (min-width: 577px)"></span>
					
						<span data-src="/content/census/en/programs-surveys/popest/jcr:content/featureicons.featureicon.3.140.medium.png/1550167479521.png" data-media=" (min-width: 801px)"></span>
					
					<noscript>
						<img src="https://www.census.gov/programs-surveys/popest/_jcr_content/featureicons.featureicon.3.png/1550167479521.png"/>
					</noscript>
				</span> 
				<div class="uscb-margin-T-sm-10 uscb-margin-T-gt-sm-30 uscb-margin-LR-16 uscb-sans-condensed uscb-font-lg uscb-line-height-24">Release Schedule</div>
			</a>
		</div>
		
		
	

	
</div></div>		


</div>

	</div>
</div>
			</div>
		</div>
		<div class="row nested-row no-gutter">
			
			<div id="landingLatest" class="uscb-landing-page-list-mobile uscb-margin-T-20 col-lg-8">
						
				
				
				
						
				
				
								
				<div class="newslisttabbed">	

	 
		
			
	
	

		

	<div class="uscb-margin-TB-15">		
	    <p class="uscb-h3 uscb-color-primary uscb-margin-TB-0">
	    	News
	    </p>
	    <div class="uscb-margin-B-30">
		    <hr class="uscb-margin-B-0 uscb-light-teal-hr"/>			
		    
		    	
		    		
	<a href="/newsroom/press-releases/2019/estimates-characteristics.html" class="uscb-list-item" title="Population Estimates Show Aging Across Race Groups Differs ">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> PRESS RELEASE</span>
			<span> | </span>
			<span>JUNE 20, 2019</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Population Estimates Show Aging Across Race Groups Differs 
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					The nation as a whole continues to grow older with the median age increasing to 38.2 years in 2018, up from 37.2 years in 2010. 
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/newsroom/press-releases/2019/estimates-characteristics/estimates-characteristics-sp.html" class="uscb-list-item" title="Nuevos estimados: el envejecimiento a través de grupos raciales">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> PRESS RELEASE</span>
			<span> | </span>
			<span>JUNE 20, 2019</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Nuevos estimados: el envejecimiento a través de grupos raciales
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					La nación continúa envejeciendo, con la edad mediana aumentando a 38.2 años de edad en 2018, en comparación con 37.2 años de edad en 2010. 
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/newsroom/press-releases/2019/characteristics-embargo-advisory.html" class="uscb-list-item" title="Census Bureau to Embargo Detailed Population Estimates">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> PRESS RELEASE</span>
			<span> | </span>
			<span>JUNE 04, 2019</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Census Bureau to Embargo Detailed Population Estimates
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					The U.S. Census Bureau will offer a two-day embargo for members of the media to view the 2018 population estimates by age, sex, race and Hispanic origin.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
	    </div>
	    
	    
	    
	    
	    	    
		
			<div class="uscb-layout-row uscb-layout-align-flex-end uscb-margin-T-20 uscb-margin-B-30 uscb-wrap">		
				<a href="/programs-surveys/popest/news.html" class="uscb-primary-button" tabindex="0">
					VIEW ALL News
				</a>																
			</div>
		
			
	    <p class="uscb-h3 uscb-color-primary uscb-margin-TB-0">
	    	Tables
	    </p>
	    <div class="uscb-margin-B-30">
		    <hr class="uscb-margin-B-0 uscb-light-teal-hr"/>			
		    
		    	
		    		
	<a href="/data/tables/time-series/demo/popest/pre-1980-national.html" class="uscb-list-item" title="National Intercensal Tables: 1900-1990">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> TABLE</span>
			
			
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            National Intercensal Tables: 1900-1990
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					These tables feature 1900-1990 intercensal estimates of population by age, sex, and race.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/data/tables/time-series/demo/popest/pre-1980-state.html" class="uscb-list-item" title="State Intercensal Tables: 1900-1990">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> TABLE</span>
			
			
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            State Intercensal Tables: 1900-1990
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					These tables feature 1900-1990 intercensal estimates of population.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/data/tables/time-series/demo/popest/pre-1980-county.html" class="uscb-list-item" title="County Intercensal Tables: 1970-1979 ">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> TABLE</span>
			
			
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            County Intercensal Tables: 1970-1979 
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					These tables feature 1970-1979 intercensal estimates of population by age, sex, and race.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
	    </div>
	    
	    
	    
	    
	    	    
		
			<div class="uscb-layout-row uscb-layout-align-flex-end uscb-margin-T-20 uscb-margin-B-30 uscb-wrap">		
				<a href="/programs-surveys/popest/data/tables.html" class="uscb-primary-button" tabindex="0">
					VIEW ALL Tables
				</a>																
			</div>
		
			
	    <p class="uscb-h3 uscb-color-primary uscb-margin-TB-0">
	    	Publications
	    </p>
	    <div class="uscb-margin-B-30">
		    <hr class="uscb-margin-B-0 uscb-light-teal-hr"/>			
		    
		    	
		    		
	<a href="/library/publications/2015/demo/p25-1142.html" class="uscb-list-item" title="Population Trends in Incorporated Places: 2000 to 2013">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> PUBLICATION</span>
			<span> | </span>
			<span>MARCH 04, 2015</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Population Trends in Incorporated Places: 2000 to 2013
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					Nearly two-thirds of Americans live in incorporated places, commonly referred to as cities.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/library/publications/2010/demo/p25-1139.html" class="uscb-list-item" title="Coastline Population Trends in the United States 1960 to 2008">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> PUBLICATION</span>
			<span> | </span>
			<span>MAY 2010</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Coastline Population Trends in the United States 1960 to 2008
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					This report examines population trends in coastline counties and those counties’ shares of coastline states for the period 1960 to 2008.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/library/publications/2010/demo/p25-1138.html" class="uscb-list-item" title="The Older Population in the United States: 2010 to 2050">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> PUBLICATION</span>
			<span> | </span>
			<span>MAY 2010</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            The Older Population in the United States: 2010 to 2050
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					Report presents info on how age structure of the overall population and the composition of the older population are expected to change over the next 4 decades.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
	    </div>
	    
	    
	    
	    
	    	    
		
			<div class="uscb-layout-row uscb-layout-align-flex-end uscb-margin-T-20 uscb-margin-B-30 uscb-wrap">		
				<a href="/programs-surveys/popest/library/publications.html" class="uscb-primary-button" tabindex="0">
					VIEW ALL Publications
				</a>																
			</div>
		
			
	    <p class="uscb-h3 uscb-color-primary uscb-margin-TB-0">
	    	Visualizations
	    </p>
	    <div class="uscb-margin-B-30">
		    <hr class="uscb-margin-B-0 uscb-light-teal-hr"/>			
		    
		    	
		    		
	<a href="/library/visualizations/2019/comm/age-race-distribution.html" class="uscb-list-item" title="A More Diverse Nation">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> VISUALIZATION</span>
			<span> | </span>
			<span>JUNE 20, 2019</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            A More Diverse Nation
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					Distribution of race and Hispanic origin by age groups.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/library/visualizations/2019/comm/housing-unit-change-2017-2018.html" class="uscb-list-item" title="Housing Unit Percent Change by County 2017 to 2018">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> VISUALIZATION</span>
			<span> | </span>
			<span>MAY 23, 2019</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Housing Unit Percent Change by County 2017 to 2018
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					Where housing units are changing.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    	
		    		
	<a href="/library/visualizations/2019/comm/housing-unit-change-2010-2018.html" class="uscb-list-item" title="Housing Unit Percent Change by County 2010 to 2018">	
		<div class="uscb-list-item uscb-margin-Top-1-neg ">		
		    		    			     			             
		    <div class="uscb-list-item-container uscb-padding-Top-1em uscb-padding-Bottom-1em uscb-flex-row-sm-100 uscb-layout-column uscb-layout-align-center">		        
		      
						
	<div>
		<p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-uppercase uscb-margin-TB-02">
			<span> VISUALIZATION</span>
			<span> | </span>
			<span>MAY 23, 2019</span>
      	</p>  
   </div>

				
		        <p class="uscb-title-3 uscb-margin-TB-02">
		            Housing Unit Percent Change by County 2010 to 2018
		        </p>
		        <p class="uscb-sub-heading-2 uscb-color-secondary-1 uscb-line-height-20-18 uscb-margin-TB-02">
					Where housing units are changing.
		        </p>
		     </div>
		     
		</div>		
	</a>
	<hr class="uscb-margin-T-0 uscb-margin-B-0 uscb-light-teal-hr"/>
		    	 
			    		     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
		    			     
		    
	    </div>
	    
	    
	    
	    
	    	    
		
			<div class="uscb-layout-row uscb-layout-align-flex-end uscb-margin-T-20 uscb-margin-B-30 uscb-wrap">		
				<a href="/programs-surveys/popest/library/visualizations.html" class="uscb-primary-button" tabindex="0">
					VIEW ALL Visualizations
				</a>																
			</div>
		
	</div>
		

</div>

			</div>
			
					<div id="landingApp" class="hidden-xs hidden-sm hidden-md col-lg-4">
						<div class="appsidebar"><div>

	 
		
			
	
	

	

	<div class="grid_quickFactsLanding">	
		<div class="quickFactsLandingMainContent" style="background:none;">
			<div><iframe src="https://www.census.gov/popclock/population_widget_200x402.php?component=density&no_scode"   width="232" height="448" frameBorder="0" allowtransparency="true"></iframe></div>
		</div>
	</div>
	
</div></div>

					</div>
			
		</div>
	</div>	
</div>
						
			
				
				<div class="col-lg-12">						
				    
	

				</div>
			
			
			
			
			<div id="pdfAndExternalLinkDiv" class="hidden-xs hidden-sm hidden-md visible-lg">
				
			</div>					
			
		</div> <!-- wrapper -->		
	</div> <!-- container-fluid -->
	
	<div class="uscb-main-container">
    	
			<div class="censusfooter universalfooter">
	<footer class="uscb-footer uscb-print-hide">
	    <div class="uscb-footer-content uscb-layout-column">
	        <div class="uscb-footer-content-top uscb-flex-col-gt-md-80 uscb-flex-col-md-95 uscb-layout-column uscb-margin-B-md-20">
	            <div class="uscb-flex-col-gt-md-75 uscb-layout-row-gt-md uscb-layout-column-md uscb-margin-T-gt-md-40 uscb-margin-T-md-30">
	                
	                
	<div class="uscb-flex-row-gt-md-50 uscb-layout-align-gt-md-start-start uscb-layout-align-md-start-start uscb-layout-column uscb-padding-L-gt-md-0 uscb-margin-B-md-30 uscb-print-hide" style="padding-right: 0px;">		
	    <p class="uscb-footer-text-title" contenteditable="false">Sign Up for Email Updates</p>	    
	    <p class="uscb-footer-text uscb-margin-T-0 uscb-margin-B-30" contenteditable="false">To sign up for updates please enter your contact information below.</p>
	    <form class="uscb-footer-subscribe uscb-layout-row-gt-md uscb-layout-column-md" action="https://public.govdelivery.com/accounts/USCENSUS/subscribers/qualify" id="GD-snippet-form" accept-charset="UTF-8" method="post">
	    	
	        <input name="utf8" type="hidden" value="&#x2713;"/>
	        <input type="hidden" name="authenticity_token" value="WYkERiwcsm2ugfWSCfiSQ0OmAlB/zVOCOSgu7FQDJa+Cbnzn5e83Uu0iBbn4c/ZxEDU3NGLA/ImfovWnn9OlYg=="/>
	        <input type="hidden" name="subscription_type" id="subscription_type" value="email"/>
	        
	        <label for="email" class="ui-helper-hidden-accessible"></label>
	        <input required type="email" name="email" id="email" placeholder="Enter your email address" contenteditable="true" style="width: 100% !important;"/>
	        
	        <button class="uscb-primary-button" name="commit" contenteditable="false" style="min-width: 105px;" value="Subscribe">
	        	Subscribe
	        </button>
	    </form>
	</div>
	
  
	                
	                <div class="uscb-flex-row-gt-md-50 uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-gt-md-end-start uscb-layout-align-md-start-start uscb-padding-LR-0">
	                    <div class="uscb-footer-side-links uscb-layout-column uscb-layout-align-gt-md-center-start uscb-layout-align-gt-md-center-start">
	                        <p class="uscb-footer-text-title">Stay Current</p>
	                        <div class="uscb-layout-column uscb-layout-align-gt-md-center-start uscb-layout-align-md-start-start">
	                        
	            				
	            				
		                            <a href="https://www.census.gov/newsroom.html">
		                                <p class="uscb-footer-text uscb-margin-TB-5">Newsroom</p>
		                            </a>
		                            
	            				
	            				
		                            <a href="https://www.census.gov/AmericaCounts">
		                                <p class="uscb-footer-text uscb-margin-TB-5">America Counts</p>
		                            </a>
		                            
	            				
	            				
		                            <a href="https://www.census.gov/newsroom/blogs.html">
		                                <p class="uscb-footer-text uscb-margin-TB-5">Blogs</p>
		                            </a>
		                            
	            				
	            				
		                            <a href="https://www.census.gov/newsroom/stories.html">
		                                <p class="uscb-footer-text uscb-margin-TB-5">Stats for Stories</p>
		                            </a>
		                            
	            				
	            				
	                        </div>
	                    </div>

	                    <div class="uscb-footer-side-links uscb-layout-column uscb-layout-align-gt-md-end-center uscb-layout-align-md-start-start uscb-hw-100 uscb-margin-T-md-20">
	    					<p class="uscb-footer-text-title">Stay Connected</p>
	                    	
		<div class="uscb-footer-social-icon-links uscb-layout-align-space-between uscb-hw-100 uscb-layout-column">

	    	
			
			
			    
			    	<div class="uscb-layout-row uscb-layout-align-gt-md-end-center uscb-hw-100 uscb-margin-TB-md-15">
				        <a href="https://www.facebook.com/uscensusbureau" class="uscb-layout-row uscb-share-icon uscb-layout-align-center-center uscb-hw-100" alt="Facebook">
				            <i class="uscb-footer-social-icon o-facebook-1"></i>
			            </a>
			    	
				        <a href="https://twitter.com/uscensusbureau" class="uscb-layout-row uscb-share-icon uscb-layout-align-center-center uscb-hw-100" alt="Twitter">
				            <i class="uscb-footer-social-icon o-twitter-1"></i>
			            </a>
			    	
				        <a href="https://www.linkedin.com/company/us-census-bureau" class="uscb-layout-row uscb-share-icon uscb-layout-align-center-center uscb-hw-100" alt="Linkedln">
				            <i class="uscb-footer-social-icon o-linkedin-1"></i>
			            </a>
			    	</div>
				
				
					<!-- to space two icons, add class 'uscb-margin-L-30' to first icon, add 'uscb-margin-R-30' to last icon -->
					
						<div class="uscb-layout-row uscb-layout-align-gt-md-end-center uscb-hw-100 uscb-margin-TB-md-15">
					       	<a href="https://www.youtube.com/user/uscensusbureau" class="uscb-layout-row uscb-share-icon uscb-layout-align-center-center uscb-hw-100 uscb-color-white uscb-margin-L-30" alt="YouTube">
					            <i class="uscb-footer-social-icon o-youtube-1"></i>
					        </a>
					        <a href="https://www.instagram.com/uscensusbureau/" class="uscb-layout-row uscb-share-icon uscb-layout-align-center-center uscb-hw-100 uscb-color-white uscb-margin-R-30" alt="Instagram">
					            <i class="uscb-footer-social-icon o-instagram-1"></i>
					        </a>
					    </div>
					
					
				
			

		</div>

 
	                    </div>
	                </div>
	            </div>
	            <div class="uscb-flex-col-gt-md-25 uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-gt-md-center-center uscb-layout-align-md-start-start uscb-padding-TB-gt-sm-12 uscb-wrap">
	            
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	
		                    <a href="https://www.census.gov/careers" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            Census Jobs
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.census.gov/quality/" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            Information Quality
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.census.gov/datalinkage" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            Data Linkage Infrastructure
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.census.gov/privacy" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            Data Protection and Privacy Policy
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.census.gov/about/policies/privacy/privacy-policy.html#accessibility" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            Accessibility
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.census.gov/foia" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            FOIA
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.commerce.gov/" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            U.S. Department of Commerce
		                    </a>
		                </div>
	            	
	            	
	            	
		                <div class="uscb-layout-row-gt-md uscb-layout-column-md uscb-layout-align-start-center">
		                	<span class="uscb-footer-link-seperator uscb-hide-md uscb-padding-LR-5">|</span>
		                    <a href="https://www.usa.gov/" class="uscb-footer-link uscb-layout-row uscb-align-center-center uscb-margin-TB-gt-md-0 uscb-margin-TB-md-5">
	                            USA.gov
		                    </a>
		                </div>
	            	
	            	
	            </div>
	        </div>
	        <div class="uscb-header-footer-container">
	            <hr class="uscb-header-footer-hr"/>
	        </div>
	        <div class="uscb-footer-content-bottom uscb-flex-col-gt-md-20 uscb-flex-col-md-5 uscb-layout-row uscb-layout-align-center-center">
	            <p class="uscb-footer-tag-line uscb-text-align-center uscb-margin-TB-10">Measuring America&#39;s People, Places, and Economy</p>
	        </div>
	    </div>
	</footer>
</div>

		
	</div>
	
	
	<div id="ratingtooljquery"></div>
	<script id="ratingtooljs" type="text/javascript" src="//www.census.gov/ratingtool/js/ratingtool.js"></script>
	
	<link rel="stylesheet" type="text/css" href="//www.census.gov/ratingtool/css/ratingtool.css"/>
	
	<div id="thumbs_div" class="ratingtool_div uscb-print-hide">
		<div id="CloseThumbs" tabindex="0">X</div>
		<div class="WasThisPageHelpful_div">
			<span class="WasThisPageHelpfulText" align="top">&nbsp;&nbsp;Is this page helpful?</span>
			<br/>
			<center>
				<img class="thumbs-valign" id="thumbsup" src="//www.census.gov/ratingtool/images/thumbsup.png" alt="Thumbs Up Image"/>
	  			<span class="YesNoText" id="yes" tabindex="0">Yes</span>&nbsp;&nbsp;&nbsp;
	  			<img class="thumbs-valign" id="thumbsdown" src="//www.census.gov/ratingtool/images/thumbsdown.png" alt="Thumbs Down Image"/>
	  			<span class="YesNoText" id="no" tabindex="0">No</span>
	  		</center>  		
		</div>
	</div>
	
	<div id="popupRating">
		<div id="closeX" tabindex="0">X</div>
		<div id="popupRatingHeadingContainer">
			<span class="popupRatingHeading"></span>
		</div>
		<div id="popupRatingContainer">
			<form id="rtform" method="post" name="rtform">
				<textarea id="RatingTool_textarea" name="message" placeholder="Tell us more." maxlength="255" tabindex="0"></textarea>
				<input id="RatingToolSubmit" type="submit" value="SUBMIT" tabindex="0"/>
			</form>
			<span class="NoThanks" tabindex="0">No, thanks</span>			
			<div id="CharCounter">
				<span id="rchars">255</span> characters remaining
			</div>
		</div>
	</div>
	
	<div id="thnx_div" class="thankyou_div">
	    <div id="closeXX" tabindex="0">X</div>
		<div class="thankyouforfeedback_div">
			<span class="thankyouText">Thank you for your feedback.</span>
			<br/>
			<span class="YesNoText" id="linkcomments" tabindex="0">Comments or suggestions?</span>
		</div>
	</div>

	
	
	<script type="text/javascript" src="/etc/designs/census/jquery.js"></script>

	
	<script type="text/javascript" src="/etc/designs/census/clientlibs.js"></script>

	<script type="text/javascript" src="/etc/designs/census/bootstrap.js"></script>

	<script type="text/javascript" src="/etc/designs/census/modernizr.js"></script>

	<script type="text/javascript" src="/etc/designs/census/universalheader.js"></script>

	<script type="text/javascript" src="/etc.clientlibs/census-core/clientlibs.js"></script>

	
		
			<script language="javascript" id="_fed_an_ua_tag" src="/etc/designs/census/clientlibs/js/federated-analytics-min.js?agency=DOC&subagency=CEN"></script>
			
<!-- Foresee Survey -->
 
<!-- End Foresee Survey -->
	
	
	
       <script charset='UTF-8'>
              window['adrum-start-time'] = new Date().getTime();
              (function(config){
                     config.appKey = 'EUM-AAB-AUN';
                  config.adrumExtUrlHttp = 'http://www.census.gov/appdynamics/adrum/';
                     config.adrumExtUrlHttps = 'https://www.census.gov/appdynamics/adrum/';
                     config.beaconUrlHttp = 'http://web-mon.csvd.census.gov:443';
                     config.beaconUrlHttps = 'https://web-mon.csvd.census.gov:443';
                     config.xd = {enable : false};
              })(window['adrum-config'] || (window['adrum-config'] = {}));
              if ('https:' === document.location.protocol) {
                     document.write(unescape('%3Cscript')
                     + " src='https://www.census.gov/appdynamics/adrum/adrum.js' "
                     + " type='text/javascript' charset='UTF-8'" 
                     + unescape('%3E%3C/script%3E'));
              } else {
                     document.write(unescape('%3Cscript')
                     + " src='http://www.census.gov/appdynamics/adrum/adrum.js' "
                     + " type='text/javascript' charset='UTF-8'" 
                     + unescape('%3E%3C/script%3E'));
              }
       </script>


	
	<script type="text/javascript">
		var referrer=document.referrer;
		if(referrer.indexOf('search-results.html')>0){
			 $("body").append("<span record=\"\'searches\', { \'searchpage\':\'SERP\'}\"></span>");
		}
	</script>	
		
	<div id="popuptext" style="display:none;">
		
		<p>By selecting this link you will leave <a href="/">www.census.gov</a>. Please check the Privacy Policy of the site you are visiting.</p>

	</div>
	<div class="cloudservices servicecomponents"><script type="text/javascript">_satellite.pageBottom();</script>
</div>
	
	
<noscript><img src="https://www.census.gov/akam/11/pixel_3bd3fa44?a=dD0yMGM0ZmEzYmM4NmYxZGJhNzVhMTUwOTc1NDc4MGMyYzA1MzczZmVhJmpzPW9mZg==" style="visibility: hidden; position: absolute; left: -999px; top: -999px;" /></noscript></body>
</html>
"""

# Use beautful soup
ps = soup(html_string, 'lxml')

#Showing our string has been set to the soup object
print(ps.prettify())

data = []
for site in ps.findAll('a', attrs={'href': re.compile("^(http*|/.)")}):
    
    link = site.get('href').strip()
    
    if link.startswith("/") :
        data.append('https://www.census.gov' + link)
    elif link.endswith('/') :
        data.append(link[:-1])
    else :
        data.append(link)
            
#Creating a pandas dataframe in order to store all of our data.        
links = pd.DataFrame({ 
    'Links' : data,
})
print(links)

links.duplicated('Links')
links = links.drop_duplicates("Links")
print(links)

links.to_csv('C:\_Projects\programming_in_python_C996\Links_Part_G.csv')