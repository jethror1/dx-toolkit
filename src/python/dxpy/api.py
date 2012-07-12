# Do not modify this file by hand.
#
# It is automatically generated by nucleus/bin/generatePythonAPIWrappers.py.
# (Run make api_wrappers to update it.)

from dxpy import DXHTTPRequest


def appAddCategories(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/addCategories' % fully_qualified_version, input_params, **kwargs)


def appAddDevelopers(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/addDevelopers' % fully_qualified_version, input_params, **kwargs)


def appAddTags(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/addTags' % fully_qualified_version, input_params, **kwargs)


def appDelete(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/delete' % fully_qualified_version, input_params, **kwargs)


def appDescribe(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/describe' % fully_qualified_version, input_params, **kwargs)


def appGet(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/get' % fully_qualified_version, input_params, **kwargs)


def appInstall(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/install' % fully_qualified_version, input_params, **kwargs)


def appListCategories(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/listCategories' % fully_qualified_version, input_params, **kwargs)


def appListDevelopers(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/listDevelopers' % fully_qualified_version, input_params, **kwargs)


def appPublish(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/publish' % fully_qualified_version, input_params, **kwargs)


def appRemoveCategories(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/removeCategories' % fully_qualified_version, input_params, **kwargs)


def appRemoveDevelopers(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/removeDevelopers' % fully_qualified_version, input_params, **kwargs)


def appRemoveTags(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/removeTags' % fully_qualified_version, input_params, **kwargs)


def appRun(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/run' % fully_qualified_version, input_params, **kwargs)


def appUninstall(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/uninstall' % fully_qualified_version, input_params, **kwargs)


def appUpdate(app_name_or_id, alias=None, input_params={}, **kwargs):
    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
    return DXHTTPRequest('/%s/update' % fully_qualified_version, input_params, **kwargs)


def appNew(input_params={}, **kwargs):
    return DXHTTPRequest('/app/new', input_params, **kwargs)


def fileAddTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params, **kwargs)


def fileAddTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTypes' % object_id, input_params, **kwargs)


def fileClose(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/close' % object_id, input_params, **kwargs)


def fileDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def fileDownload(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/download' % object_id, input_params, **kwargs)


def fileGetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/getDetails' % object_id, input_params, **kwargs)


def fileListProjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listProjects' % object_id, input_params, **kwargs)


def fileRemoveTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTags' % object_id, input_params, **kwargs)


def fileRemoveTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTypes' % object_id, input_params, **kwargs)


def fileRename(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/rename' % object_id, input_params, **kwargs)


def fileSetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setDetails' % object_id, input_params, **kwargs)


def fileSetProperties(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params, **kwargs)


def fileSetVisibility(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setVisibility' % object_id, input_params, **kwargs)


def fileUpload(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/upload' % object_id, input_params, **kwargs)


def fileNew(input_params={}, **kwargs):
    return DXHTTPRequest('/file/new', input_params, **kwargs)


def gtableAddRows(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addRows' % object_id, input_params, **kwargs)


def gtableAddTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params, **kwargs)


def gtableAddTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTypes' % object_id, input_params, **kwargs)


def gtableClose(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/close' % object_id, input_params, **kwargs)


def gtableDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def gtableExtend(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/extend' % object_id, input_params, **kwargs)


def gtableGet(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/get' % object_id, input_params, **kwargs)


def gtableGetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/getDetails' % object_id, input_params, **kwargs)


def gtableListProjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listProjects' % object_id, input_params, **kwargs)


def gtableNextPart(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/nextPart' % object_id, input_params, **kwargs)


def gtableRemoveTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTags' % object_id, input_params, **kwargs)


def gtableRemoveTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTypes' % object_id, input_params, **kwargs)


def gtableRename(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/rename' % object_id, input_params, **kwargs)


def gtableSetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setDetails' % object_id, input_params, **kwargs)


def gtableSetProperties(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params, **kwargs)


def gtableSetVisibility(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setVisibility' % object_id, input_params, **kwargs)


def gtableNew(input_params={}, **kwargs):
    return DXHTTPRequest('/gtable/new', input_params, **kwargs)


def inviteAccept(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/accept' % object_id, input_params, **kwargs)


def inviteApprove(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/approve' % object_id, input_params, **kwargs)


def inviteDecline(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/decline' % object_id, input_params, **kwargs)


def inviteDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def inviteDestroy(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/destroy' % object_id, input_params, **kwargs)


def inviteReject(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/reject' % object_id, input_params, **kwargs)


def jobDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def jobStreamLog(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/streamLog' % object_id, input_params, **kwargs)


def jobTerminate(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/terminate' % object_id, input_params, **kwargs)


def jobNew(input_params={}, **kwargs):
    return DXHTTPRequest('/job/new', input_params, **kwargs)


def notificationsGet(input_params={}, **kwargs):
    return DXHTTPRequest('/notifications/get', input_params, **kwargs)


def notificationsMarkRead(input_params={}, **kwargs):
    return DXHTTPRequest('/notifications/markRead', input_params, **kwargs)


def programAddTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params, **kwargs)


def programAddTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTypes' % object_id, input_params, **kwargs)


def programClose(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/close' % object_id, input_params, **kwargs)


def programDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def programGet(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/get' % object_id, input_params, **kwargs)


def programGetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/getDetails' % object_id, input_params, **kwargs)


def programListProjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listProjects' % object_id, input_params, **kwargs)


def programRemoveTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTags' % object_id, input_params, **kwargs)


def programRemoveTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTypes' % object_id, input_params, **kwargs)


def programRename(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/rename' % object_id, input_params, **kwargs)


def programRun(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/run' % object_id, input_params, **kwargs)


def programSetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setDetails' % object_id, input_params, **kwargs)


def programSetProperties(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params, **kwargs)


def programSetVisibility(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setVisibility' % object_id, input_params, **kwargs)


def programNew(input_params={}, **kwargs):
    return DXHTTPRequest('/program/new', input_params, **kwargs)


def projectAddTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params, **kwargs)


def projectClone(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/clone' % object_id, input_params, **kwargs)


def projectDecreasePermissions(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/decreasePermissions' % object_id, input_params, **kwargs)


def projectDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def projectDestroy(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/destroy' % object_id, input_params, **kwargs)


def projectInvite(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/invite' % object_id, input_params, **kwargs)


def projectJoin(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/join' % object_id, input_params, **kwargs)


def projectLeave(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/leave' % object_id, input_params, **kwargs)


def projectListFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listFolder' % object_id, input_params, **kwargs)


def projectMove(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/move' % object_id, input_params, **kwargs)


def projectNewFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/newFolder' % object_id, input_params, **kwargs)


def projectRemoveFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeFolder' % object_id, input_params, **kwargs)


def projectRemoveObjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeObjects' % object_id, input_params, **kwargs)


def projectRemoveTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTags' % object_id, input_params, **kwargs)


def projectRenameFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/renameFolder' % object_id, input_params, **kwargs)


def projectSetProperties(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params, **kwargs)


def projectSubscribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/subscribe' % object_id, input_params, **kwargs)


def projectUnsubscribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/unsubscribe' % object_id, input_params, **kwargs)


def projectUpdate(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/update' % object_id, input_params, **kwargs)


def projectNew(input_params={}, **kwargs):
    return DXHTTPRequest('/project/new', input_params, **kwargs)


def recordAddTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params, **kwargs)


def recordAddTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTypes' % object_id, input_params, **kwargs)


def recordClose(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/close' % object_id, input_params, **kwargs)


def recordDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def recordGetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/getDetails' % object_id, input_params, **kwargs)


def recordListProjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listProjects' % object_id, input_params, **kwargs)


def recordRemoveTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTags' % object_id, input_params, **kwargs)


def recordRemoveTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTypes' % object_id, input_params, **kwargs)


def recordRename(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/rename' % object_id, input_params, **kwargs)


def recordSetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setDetails' % object_id, input_params, **kwargs)


def recordSetProperties(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params, **kwargs)


def recordSetVisibility(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setVisibility' % object_id, input_params, **kwargs)


def recordNew(input_params={}, **kwargs):
    return DXHTTPRequest('/record/new', input_params, **kwargs)


def requestApprove(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/approve' % object_id, input_params, **kwargs)


def requestDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def requestDestroy(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/destroy' % object_id, input_params, **kwargs)


def requestReject(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/reject' % object_id, input_params, **kwargs)


def systemFindAffiliates(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findAffiliates', input_params, **kwargs)


def systemFindApps(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findApps', input_params, **kwargs)


def systemFindDataObjects(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findDataObjects', input_params, **kwargs)


def systemFindDiscitems(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findDiscitems', input_params, **kwargs)


def systemFindFeeditems(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findFeeditems', input_params, **kwargs)


def systemFindInvites(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findInvites', input_params, **kwargs)


def systemFindJobs(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findJobs', input_params, **kwargs)


def systemFindProjects(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findProjects', input_params, **kwargs)


def systemFindRequests(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findRequests', input_params, **kwargs)


def systemFindUsers(input_params={}, **kwargs):
    return DXHTTPRequest('/system/findUsers', input_params, **kwargs)


def systemGetLog(input_params={}, **kwargs):
    return DXHTTPRequest('/system/getLog', input_params, **kwargs)


def systemGetProjectTags(input_params={}, **kwargs):
    return DXHTTPRequest('/system/getProjectTags', input_params, **kwargs)


def systemGlobalSearch(input_params={}, **kwargs):
    return DXHTTPRequest('/system/globalSearch', input_params, **kwargs)


def systemShortenURL(input_params={}, **kwargs):
    return DXHTTPRequest('/system/shortenURL', input_params, **kwargs)


def tableAddColumns(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addColumns' % object_id, input_params, **kwargs)


def tableAddIndices(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addIndices' % object_id, input_params, **kwargs)


def tableAddRows(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addRows' % object_id, input_params, **kwargs)


def tableAddTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTags' % object_id, input_params, **kwargs)


def tableAddTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/addTypes' % object_id, input_params, **kwargs)


def tableClose(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/close' % object_id, input_params, **kwargs)


def tableDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def tableGet(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/get' % object_id, input_params, **kwargs)


def tableGetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/getDetails' % object_id, input_params, **kwargs)


def tableListProjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listProjects' % object_id, input_params, **kwargs)


def tableModifyColumn(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/modifyColumn' % object_id, input_params, **kwargs)


def tableRemoveColumns(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeColumns' % object_id, input_params, **kwargs)


def tableRemoveIndices(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeIndices' % object_id, input_params, **kwargs)


def tableRemoveRows(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeRows' % object_id, input_params, **kwargs)


def tableRemoveTags(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTags' % object_id, input_params, **kwargs)


def tableRemoveTypes(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeTypes' % object_id, input_params, **kwargs)


def tableRename(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/rename' % object_id, input_params, **kwargs)


def tableSetDetails(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setDetails' % object_id, input_params, **kwargs)


def tableSetProperties(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setProperties' % object_id, input_params, **kwargs)


def tableSetVisibility(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/setVisibility' % object_id, input_params, **kwargs)


def tableUpdate(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/update' % object_id, input_params, **kwargs)


def tableNew(input_params={}, **kwargs):
    return DXHTTPRequest('/table/new', input_params, **kwargs)


def userDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def userUpdate(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/update' % object_id, input_params, **kwargs)


def workspaceClone(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/clone' % object_id, input_params, **kwargs)


def workspaceDescribe(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/describe' % object_id, input_params, **kwargs)


def workspaceDestroy(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/destroy' % object_id, input_params, **kwargs)


def workspaceListFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/listFolder' % object_id, input_params, **kwargs)


def workspaceMove(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/move' % object_id, input_params, **kwargs)


def workspaceNewFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/newFolder' % object_id, input_params, **kwargs)


def workspaceRemoveFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeFolder' % object_id, input_params, **kwargs)


def workspaceRemoveObjects(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/removeObjects' % object_id, input_params, **kwargs)


def workspaceRenameFolder(object_id, input_params={}, **kwargs):
    return DXHTTPRequest('/%s/renameFolder' % object_id, input_params, **kwargs)

