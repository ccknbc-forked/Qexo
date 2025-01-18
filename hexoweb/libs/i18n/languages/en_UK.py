"""
@Project   : en_UK
@Author    : abudu & Deepseek
@Blog      : https://www.oplog.cn
"""

from ..core import Language


class Main(Language):
    name = 'en_UK'
    name_local = "English(United Kingdom)"
    default = {
        "name": name,
        "data": {
            "ADD": "Add",
            "ADD_CATEGORY": "Add Category",
            "ADD_SUCCESS": "Added successfully!",
            "ADD_TAG": "Add Tag",
            "ADVANCED": "Advanced",
            "ADVANCED_SETTINGS": "Advanced Settings",
            "ADVANCED_SETTINGS_LABEL": "Advanced Settings",
            "API_VERIFY_FAILED": "API verification failed, access IP: {}",
            "AUTHOR": "Author",
            "AUTO_PROVIDER_FAILED": "Error in automatic generation of PROVIDER, please check the configuration and submit",
            "BACKUP": "Backup File",
            "BOTTOM_PH": "If multiple levels, please use JSON format",
            "CACHE": "Cache",
            "CACHE_CLEAN_REQUEST": "Are you sure you want to clear all caches?",
            "CANCEL": "Cancel",
            "CAPTCHA_FAILED": "Captcha verification failed!",
            "CAPTCHA_GET_FAILED": "Failed to get",
            "CAPTCHA_NO": "No captcha information received",
            "CAPTCHA_RESULT": "reCaptcha{} result: {}",
            "CATEGORY_EXITS": "Category already exists!",
            "CHANGE_LANGUAGE": "Change Language",
            "CLEAN_FLINKS_FAILED": "No hidden friend links",
            "CLEAN_FLINKS_SUCCESS": "Successfully cleaned {} friend links",
            "CLEAR_ALL": "Clear All",
            "CLOSE": "Close",
            "CLOUD_SCRIPTS": "Cloud Script Library",
            "COMMAND": "Command",
            "CONFIG": "Configuration",
            "CONFIGS_LIST": "Configuration List",
            "CONFIG_LABEL": "All Configurations",
            "CONFIG_NAME": "Configuration Name",
            "CONFIRM": "Confirm",
            "CONFIRM_CLEAN_FLINK": "Are you sure you want to clean hidden links? This operation is irreversible",
            "CONFIRM_DEL_CUSTOM": "Are you sure you want to delete the {0} field? This operation is irreversible",
            "CONFIRM_FIX": "Are you sure you want to attempt automatic repair of the program? This will check and create/delete the corresponding fields",
            "CONFIRM_RUN": "Are you sure you want to run {0}? This operation cannot be aborted",
            "CONSOLE": "Console",
            "CONTENT": "Content",
            "CURRENT_ENV": "Current Environment",
            "CUSTOM": "Custom",
            "CUSTOMIZE": "Customize",
            "CUSTOMIZE_LABEL": "Dashboard Style Configuration Items",
            "CUSTOM_LABEL": "Custom Field",
            "CUSTOM_LIST": "Custom Fields",
            "DARKMODE": "Light / Dark",
            "DASHBOARD": "Dashboard",
            "DELETING": "Deleting...",
            "DEL_CONFIRM_1": "Are you sure you want to delete",
            "DEL_CONFIRM_2": "? This operation is irreversible",
            "PUBLISH_CONFIRM_1": "Are you sure you want to publish",
            "PUBLISH_CONFIRM_2": "?",
            "UNPUBLISH_CONFIRM_1": "Are you sure you want to unpublish",
            "UNPUBLISH_CONFIRM_2": "?",
            "DEL_FAILED": "Delete failed",
            "DEL_POST_INDEX": "Delete Post Detail Index",
            "DEL_REMOTE": "Delete Remote File",
            "DEL_SUCCESS": "Deleted successfully!",
            "DEL_SUCCESS_AND_DEPLOY": "Deleted successfully and deployment submitted!",
            "DEL_TMP": "Delete Temporary Directory",
            "DEL_VALUE": "Delete Field",
            "DESCRIPTION": "Description",
            "DOC": "Documentation",
            "DRAFT": "Draft",
            "DRAFT_SAVE_SUCCESS": "Draft saved successfully!",
            "DRAFT_SAVE_SUCCESS_AND_DEPLOY": "Draft saved successfully and deployment submitted!",
            "EDIT": "Edit",
            "EDIT_CONFIG": "Edit Configuration",
            "EDIT_FLINK": "Edit Friend Link",
            "EDIT_PAGE": "Edit Page",
            "EDIT_PAGE_LABEL": "Edit Page",
            "EDIT_POST": "Edit Post",
            "EDIT_POST_LABEL": "Edit Post",
            "EDIT_SIDEBAR": "Edit Sidebar",
            "EDIT_SUCCESS": "Edited successfully!",
            "EDIT_TALK": "Edit Talk",
            "EDIT_TALK_LABEL": "Edit Talk",
            "EDIT_TALK_PH": "Write your talk here...",
            "ELEVATOR_ERROR": "Error in automatic update migration program: {}",
            "ELEVATOR_START": "Starting automatic update migration program... from {}",
            "ERROR": "Error",
            "ERROR_GETTING_PROVIDER": "Error getting PROVIDER",
            "EXCERPT_FAILED": "Failed to get excerpt: ",
            "EXCERPT_LOADING": "Loading excerpt...",
            "EXCERPT_LOCAL_LENGTH": "Excerpt Length",
            "EXCERPT_LOCAL_LENGTH_PH": "Length to truncate",
            "EXCERPT_TIANLI_KEY": "User Key",
            "EXCERPT_TIANLI_KEY_PH": "User key obtained from Aifadian",
            "EXCERPT_TIANLI_LENGTH": "Send Length",
            "EXCERPT_TIANLI_LENGTH_PH": "Length of content sent to the server",
            "EXPORT": "Export",
            "FIND_INDEX_FAILED": "Update failed: Index directory not found",
            "FIND_INDEX_SUCCESS": "Index directory found",
            "FIND_UPDATE_INDEX": "Extraction complete, looking for Index directory",
            "FINISH": "Finish",
            "FIXING": "Repairing... Please wait",
            "FIX_DISPLAY": "Attempted automatic repair of {} fields, please check and modify the configuration later",
            "FIX_SUCCESS": "Repaired {} settings",
            "FIX_VALUE": "Fix Field",
            "FLINK": "Friend Link",
            "FLINKS_LIST": "Friend Links",
            "FLINK_LABEL": "Friend Links",
            "FORCE_MSG": "Are you sure you want to force submit?",
            "FORCE_SUBMIT": "Force Submit",
            "FRONT_MATTER_GET_ERROR": "FrontMatter parsing error: {}",
            "GET_ADVANCED_SETTINGS_FAILED": "Error getting advanced settings: {}",
            "GET_CUSTOM_FAILED": "Error getting custom fields: {}",
            "GET_PAGE_SCAFFOLD_FAILED": "Failed to get page template, error message: {}",
            "GET_POST_SCAFFOLD_FAILED": "Failed to get post template, error message: {}",
            "GET_SCRIPTS_FAILED": "Error getting online function library: {}",
            "GET_SETTINGS_FAILED": "Error getting settings, redirecting to settings update page",
            "GET_UPDATE_FAILED": "Failed to get update",
            "GET_UPDATE_SUCCESS": "Update retrieved successfully",
            "HAS_MSG_TIP_1": "You have",
            "HAS_MSG_TIP_2": "unread messages",
            "HEADER": "Header",
            "HELP": "Help",
            "HELP_LABEL": "Need help?",
            "HELP_TIP": "Click here to find documentation",
            "HEXO_CONFIG": "\nDetected Hexo configuration file",
            "HEXO_CONFIG_FAILED": "\nHexo configuration file not detected",
            "HEXO_CONFIG_UPDATE": "\nHexo configuration file updated successfully",
            "HEXO_CONFIG_UPDATE_FAILED": "\nConfiguration validation failed",
            "HEXO_INDEX_FAILED": "\nDetected index.html, this may not be the correct repository",
            "HEXO_PACKAGE": "\nDetected package.json",
            "HEXO_PACKAGE_FAILED": "\npackage.json not detected",
            "HEXO_SOURCE": "\nDetected source directory",
            "HEXO_SOURCE_FAILED": "\nSource directory not detected",
            "HEXO_THEME": "\nDetected theme directory",
            "HEXO_THEME_FAILED": "\nTheme directory not detected",
            "HEXO_TOKEN_FAILED": "Remote connection error! Please check the Token",
            "HEXO_VERSION": "Detected Hexo version: {}",
            "HEXO_VERSION_FAILED": "Hexo not detected",
            "HOME": "Home",
            "ICON": "Icon",
            "ID_CODE": "Identification Code",
            "IMAGE": "Image",
            "IMAGES_LIST": "Image List",
            "IMAGE_DEL_SUCCESS": "Local record deleted",
            "IMAGE_LABEL": "All Images",
            "IMAGE_LINK": "Image Link",
            "IMAGE_NAME": "Image Name",
            "IMPORT": "Import",
            "IMPORT_WARN": "After import, you will lose all existing information, please confirm!",
            "INDEX_GITHUB_TIP": "Support the author",
            "INDEX_GUIDE_LABEL": "What do you want to do now?",
            "INDEX_GUIDE_LABEL_1": "New Post",
            "INDEX_GUIDE_LABEL_2": "New Page",
            "INDEX_GUIDE_LABEL_3": "New Friend Link",
            "INDEX_GUIDE_LABEL_4": "New Talk",
            "INDEX_GUIDE_TIP_1_P1": "Write your",
            "INDEX_GUIDE_TIP_1_P2": "new idea",
            "INDEX_GUIDE_TIP_2_P1": "Create your",
            "INDEX_GUIDE_TIP_2_P2": "new page",
            "INDEX_GUIDE_TIP_3_P1": "Add your",
            "INDEX_GUIDE_TIP_3_P2": "new friend",
            "INDEX_GUIDE_TIP_4_P1": "Share your",
            "INDEX_GUIDE_TIP_4_P2": "new news",
            "INDEX_IMAGE_LABEL": "Total Images",
            "INDEX_IMAGE_TIP": "Management",
            "INDEX_POST_LABEL": "Total Posts",
            "INDEX_POST_TIP": "Write a post today?",
            "INDEX_RANDOM_POSTS": "Random Posts",
            "INDEX_RECENT_IMAGES": "Recent Images",
            "INDEX_RECENT_POSTS": "Recent Posts",
            "INDEX_VERSION_HASNEW": "Update detected",
            "INDEX_VERSION_LABEL": "Current Version",
            "INDEX_VERSION_TIP": "Up to date",
            "INIT": "Initialize",
            "INIT_2_1": "API Key",
            "INIT_2_1_PH": "Leave blank to auto-generate",
            "INIT_2_2": "Username",
            "INIT_2_2_PH": "Set username",
            "INIT_2_3": "Password",
            "INIT_2_3_PH": "Set password",
            "INIT_2_4": "Confirm Password",
            "INIT_2_4_PH": "Re-enter to confirm password",
            "INIT_3_1": "Provider",
            "INIT_3_2": "Use Configuration",
            "INIT_4_1": "Vercel Key",
            "INIT_4_2": "Project ID",
            "INIT_BLOG": "Blog Configuration",
            "INIT_FINISH": "Congratulations, you have completed the initialization",
            "INIT_IMAGE": "Image Configuration",
            "INIT_LOGIN_MSG_1": "Please remember your login information:",
            "INIT_LOGIN_MSG_2": "Username: ",
            "INIT_LOGIN_MSG_3": "Password: Your set value",
            "INIT_LOGIN_MSG_4": "Login to the console",
            "INIT_PROVIDER_FAILED": "Error initializing PROVIDER: {}",
            "INIT_SUCCESS": "Initialization completed, redirecting to the homepage",
            "INIT_USER": "User Configuration",
            "INIT_USER_FAILED": "Error initializing username and password: {}",
            "INIT_VERCEL": "Vercel Configuration",
            "INIT_VERCEL_FAILED": "Error initializing Vercel: {}",
            "INIT_WELCOME": "Welcome! Please select a language to start the initialization",
            "INPUT_ARGV": "Please enter parameters",
            "JUMPED": "Skipped",
            "JUMP_UPDATE": "Update configuration detected, redirecting to the settings update page",
            "JUMP_UPDATE_FAILED": "Failed to detect configuration update, redirecting to the update page",
            "LEAVE_CONFIRM": "Are you sure you want to leave?",
            "LINK": "Link",
            "LOADING": "Loading...",
            "LOCAL": "Local",
            "LOCAL_UPDATE_SUCCESS": "Update completed, thread will restart in five seconds",
            "LOGIN": "Login",
            "LOGIN_FAILED": "Login information error",
            "LOGIN_FAILED_1": "Username cannot be empty! ",
            "LOGIN_FAILED_2": "Password cannot be empty! ",
            "LOGIN_FAILED_3": "Please complete the verification! ",
            "LOGIN_SUCCESS": "Login successful, waiting for redirection",
            "LOGOUT": "Logout",
            "LOGOUT_SUCCESS": "Logout successful",
            "LOVE": "Like",
            "MEASURE_IMAGE": "images",
            "MEASURE_LINK": "links",
            "MEASURE_POST": "posts",
            "MIGRATE": "Migrate",
            "MIGRATE_CONFIG_SUCCESS": "Configuration migration completed!",
            "MIGRATE_CUSTOM_SUCCESS": "Custom fields migration completed!",
            "MIGRATE_DB": "Starting database migration",
            "MIGRATE_FAILED": "Migration of {} failed: {}",
            "MIGRATE_FLINKS_SUCCESS": "Friend links migration completed!",
            "MIGRATE_IMAGE_SUCCESS": "Images migration completed!",
            "MIGRATE_LABEL": "Migrate Configuration",
            "MIGRATE_MSG_SUCCESS": "Messages migration completed!",
            "MIGRATE_POST_SUCCESS": "Post detail index migration completed!",
            "MIGRATE_PV_SUCCESS": "PV migration completed!",
            "MIGRATE_SUCCESS": "All migrations completed!",
            "MIGRATE_TALKS_SUCCESS": "Talks migration completed!",
            "MIGRATE_UV_SUCCESS": "UV migration completed!",
            "MSG_LOADING": "Loading messages...",
            "MSG_LOAD_ERROR": "Failed to load messages",
            "NAME": "Name",
            "NAVBAR_FIX": "Fix Navbar",
            "NETWORK_ERROR": "Network error!",
            "NEW_FLINK": "New Friend Link",
            "NEW_NAME": "New Name",
            "NEW_PAGE": "New Page",
            "NEW_PAGE_LABEL": "New Page",
            "NEW_POST": "New Post",
            "NEW_POST_LABEL": "New Post",
            "NEW_VALUE": "New Field",
            "NEXT": "Next",
            "NEXT_PAGE": "Next Page",
            "NEW ": " New",
            "NEW_PH ": " The file will be saved as",
            "NOT_INIT": "Initialization configuration not completed, redirecting to the initialization page",
            "NO_MSG_TIP": "You currently have no messages~",
            "NO_NEXT_PAGE": "This is the last page",
            "NO_OTHER_ARGV": "No other parameters",
            "NO_PAGE_NAME": "Please enter a correct page name in the top bar!",
            "NO_PERMISSION": "Sub-user does not support this operation!",
            "NO_POST_NAME": "Please enter a correct post name in the top bar!",
            "NO_PREV_PAGE": "This is the first page",
            "ONEKEY_UPDATE": "One-click Update",
            "OPERATION": "Operation",
            "OPERATION_SUCCESS": "Operation successful!",
            "OTHER_ARGV": "Other Parameters",
            "PAGE": "Page",
            "PAGES_LIST": "Page List",
            "PAGE_403_LABEL": "Error! Error 403",
            "PAGE_403_TIP": "Verification error - Please confirm if you have permission",
            "PAGE_404": "Page does not exist: {}",
            "PAGE_404_LABEL": "Error! Error 404",
            "PAGE_404_TIP": "Page not found - ",
            "PAGE_500": "Server error: {}",
            "PAGE_500_LABEL": "Error! Error 500",
            "PAGE_500_TIP": "Error message：",
            "PAGE_ARGV_LABEL": "Page Parameters",
            "PAGE_EXIST": "Page already exists!",
            "PAGE_LABEL": "All Pages",
            "PAGE_NAME": "Page Name",
            "PASSWORD": "Password",
            "POST": "Post",
            "POSTS_LIST": "Post List",
            "POST_ARGV_LABEL": "Post Parameters",
            "POST_EXIST": "Post already exists!",
            "POST_LABEL": "All Posts",
            "POST_NAME": "Post Name",
            "PREV_PAGE": "Previous Page",
            "PROJECT_PAGE": "Project Page",
            "PROVIDER_NO_SUPPORT": "Provider not supported!",
            "PROVIDER_VERIFY_ERROR": "Configuration verification error",
            "PROVIDER_VERIFY_SUCCESS": "Provider verification result: {}",
            "PUBLISHED": "Published",
            "PUBLISH_SUCCESS": "Published successfully!",
            "UNPUBLISH_SUCCESS": "Unpublished Successfully!",
            "PURGE_ALL_CACHE_SUCCESS": "All caches cleared successfully",
            "PURGE_CACHE": "Purge Cache",
            "QEXO_MSG": "Qexo Messages",
            "READ_FILE": "Read File",
            "REBUILD_CACHE_SUCCESS": "{} cache rebuilt successfully",
            "RENAME": "Rename",
            "RENAME_SUCCESS": "Renamed successfully!",
            "RENAME_SUCCESS_AND_DEPLOY": "Renamed successfully and deployment submitted!",
            "REQUIRED": "Required",
            "RESET": "Reset",
            "RESET_PASSWORD_NO": "Please enter a correct password!",
            "RESET_PASSWORD_NO_MATCH": "Passwords do not match!",
            "RESET_PASSWORD_NO_OLD": "Old password incorrect!",
            "RESET_PASSWORD_NO_PASSWORD": "Password cannot be empty!",
            "RESET_PASSWORD_NO_USERNAME": "Please enter a correct username!",
            "RESULT": "Result",
            "RETRY": "Retry",
            "RUNNING": "Running...",
            "SAVE_CUSTOM": "Save Custom Fields",
            "SAVE_FAILED": "Save failed!",
            "SAVE_SETTING": "Save Settings",
            "SAVE_SUCCESS": "Saved successfully!",
            "SAVE_SUCCESS_AND_DEPLOY": "Saved successfully and deployment submitted!",
            "SAVE_SUCCESS_REDIRECT": "Saved successfully, redirecting...",
            "SAVING": "Saving...",
            "SCRIPTS_LABEL": "Cloud Commands",
            "SCRIPTS_LIST": "Online Function Library",
            "SCRIPT_ARGV_FAILED": "Please enter correct parameters!",
            "SCRIPT_RUN": "Running cloud command: {}",
            "SCRIPT_RUN_SUCCESS": "Run successful",
            "SCRIPT_RUN_SUCCESS_LOG": "Execution of {} successful: {}",
            "SEARCH": "Search",
            "SEARCH_CONFIG": "Search Configuration",
            "SEARCH_CUSTOM": "Search Fields",
            "SEARCH_FLINK": "Search Friend Links",
            "SEARCH_IMAGE": "Search Images",
            "SEARCH_ITEM": "Search Item",
            "SEARCH_PAGE": "Search Pages",
            "SEARCH_POST": "Search Posts",
            "SEARCH_SCRIPT": "Search Commands",
            "SEARCH_SETTINGS": "Search Settings",
            "SEARCH_TALK": "Search Talks",
            "SETTINGS": "Settings",
            "SETTINGS_LABEL": "Modify Configuration",
            "SET_ABBRLINK": "Short Link Settings",
            "SET_ABBRLINK_1": "Short Link Algorithm",
            "SET_ABBRLINK_2": "Short Link Base",
            "SET_API": "API Settings",
            "SET_API_1": "API Key",
            "SET_API_1_PH": "Leave blank to remain unchanged",
            "SET_API_2": "Enable Friend Link Request API",
            "SET_API_3": "Use reCaptcha to verify friend link requests",
            "SET_API_4": "reCaptcha Key",
            "SET_API_4_PH": "reCaptchaV3 server token",
            "SET_BLOG": "Blog Settings",
            "SET_BLOG_1": "Provider",
            "SET_BLOG_2": "Use Configuration",
            "SET_CDN": "CDN Settings",
            "SET_CDN_1": "CDN Provider",
            "SET_CUSTOM": "Custom Settings",
            "SET_CUSTOM_1": "Site Name",
            "SET_CUSTOM_1_PH": "Defaults to Hexo Dashboard",
            "SET_CUSTOM_2": "Site Connector",
            "SET_CUSTOM_2_PH": "Defaults to “ - ”",
            "SET_CUSTOM_3": "Site Logo",
            "SET_CUSTOM_3_PH": "Defaults to qexo.png under images",
            "SET_CUSTOM_4": "Site Icon",
            "SET_CUSTOM_4_PH": "Defaults to icon.png under images",
            "SET_CUSTOM_5": "Dark Logo",
            "SET_CUSTOM_5_PH": "Defaults to qexo-dark.png under images",
            "SET_EXCERPT": "Excerpt Settings",
            "SET_EXCERPT_1": "Extraction Method",
            "SET_EXCERPT_2": "Automatic Extraction",
            "SET_EXCERPT_3": "Saved Field",
            "SET_EXCERPT_3_PH": "Usually excerpt",
            "SET_IMAGE": "Image Settings",
            "SET_IMAGE_1": "Image Type",
            "SET_NOTIFY": "Notification Settings",
            "SET_NOTIFY_1": "Provider",
            "SET_SECURE": "Security Settings",
            "SET_SECURE_1": "Login Page reCaptchaV3 User Key",
            "SET_SECURE_1_PH": "Leave blank to disable the feature",
            "SET_SECURE_2": "Login Page reCaptchaV3 Server Key",
            "SET_SECURE_2_PH": "Leave blank to disable the feature",
            "SET_SECURE_3": "Login Page reCaptchaV2 User Key",
            "SET_SECURE_3_PH": "Leave blank to disable the feature",
            "SET_SECURE_4": "Login Page reCaptchaV2 Server Key",
            "SET_SECURE_4_PH": "Leave blank to disable the feature",
            "SET_STATISTICS": "Statistics Settings",
            "SET_STATISTICS_1": "Enable Statistics API",
            "SET_STATISTICS_2": "Statistics Secure Domains",
            "SET_STATISTICS_2_PH": "Enter domain keywords, comma-separated",
            "SET_USER": "User Settings",
            "SET_USER_1": "Old Password",
            "SET_USER_1_PH": "Please enter the old password",
            "SET_USER_2": "New Username",
            "SET_USER_2_PH": "Please enter the new username",
            "SET_USER_3": "New Password",
            "SET_USER_3_PH": "Please enter the new password",
            "SET_USER_4": "Confirm Password",
            "SET_USER_4_PH": "Re-enter to confirm the password",
            "SET_WEBHOOK": "One-click Setup WEBHOOK",
            "SIDEBAR_COLOR": "Sidebar Color",
            "SIDEBAR_EDIT_1": "Content before the colon",
            "SIDEBAR_EDIT_2": "Description Title",
            "SIDEBAR_EDIT_3": "Icon Used",
            "SIDEBAR_TYPE": "Sidebar Type",
            "SIDEBAR_TYPE_LABEL": "Choose between two styles",
            "SIDEBAR_TYPE_TIP": "You can only change the style on desktop",
            "SIZE": "Size",
            "SKIP": "Skip",
            "START": "Start",
            "START_COPY": "Deletion complete, copying files...",
            "START_DEL": "Starting file deletion...",
            "START_EXTRACT_UPDATE": "Update download complete, starting extraction",
            "START_LOCAL_UPDATE": "Starting update, using local solution, preparing temporary directory",
            "START_VERCEL_UPDATE": "Starting update, using Vercel solution",
            "STATUS": "Status",
            "STILL_IMPORT": "Continue",
            "SUBMIT": "Submit",
            "SUPPORT": "Support",
            "SYSTEM_ERROR": "The program encountered an error!",
            "TAGS": "Tags",
            "TAG_EXITS": "Tag already exists!",
            "TALK": "Talk",
            "TALKS_LIST": "Talk List",
            "TALK_ARGV_LABEL": "Talk Parameters",
            "TALK_LABEL": "All Talks",
            "TEST": "Test",
            "TEST_MESSAGE": "If you received this message, it means your message configuration was successful",
            "THANK_LABEL": "Thank you for your Star!",
            "TIME": "Time",
            "TIPS": "Tips",
            "UNKNOWN_SIDEBAR": "Unknown Sidebar",
            "UNTITLED": "Untitled",
            "UPDATE": "Update",
            "UPDATED_AT": "Updated At",
            "UPDATED_AT_PH": "Update Time",
            "UPDATE_CHANNEL": "Update Channel",
            "UPDATE_CONFIG": "Configuration Update",
            "UPDATE_CONTENT": "Update detected: {}<br>{}<p>Go to <object><a href=\"/settings.html\">Settings</a></object> for online update</p>",
            "UPDATE_LABEL": "Program Update",
            "UPDATE_LIB": "Starting library update...",
            "UPDATE_NO_CHANNEL": "No such update channel",
            "UPDATE_POST_INDEX": "Update Post Detail Index",
            "UPDATE_QUEUING": "Update failed: There is a deployment in progress",
            "UPDATE_SUCCESS": "Update successful",
            "UPDATE_SUCCESS_DISPLAY": "Update successful, please wait for automatic deployment!",
            "UPDATING": "Updating...",
            "UPLOAD": "Upload",
            "UPLOAD_FAILED": "Upload failed!",
            "UPLOAD_SUCCESS": "Upload successful!",
            "UPLOAD_TIP": "Upload Image",
            "USERNAME": "Username",
            "USER_IS_NOT_STAFF": "Sub-user {} attempted to access {} but was denied",
            "USER_IS_NOT_STAFF_DEL": "Sub-user {} attempted to delete {} but was denied",
            "USER_IS_NOT_STAFF_MODIFY": "Sub-user {} attempted to modify {} but was denied",
            "USER_IS_NOT_STAFF_RENAME": "Sub-user {} attempted to rename {} but was denied",
            "VALUE": "Field",
            "VALUE_NAME": "Field Name",
            "VERIFY_FAILED": "Verification failed",
            "WARN": "Warning",
            "WARN_RESET": "Are you sure you want to reset the custom configuration? This operation is irreversible",
            "WARN_WEBHOOK": "Are you sure you want to automatically create Webhook events? This will clear all your original repository's Webhook events",
            "WELCOME": "Welcome",
            "WIKI_LABEL": "View Documentation"
        }
    }
