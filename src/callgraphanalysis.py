

# AS DEFINED at https://developer.android.com/reference/packages.html
API_LIST = ["android",
            "android.accessibilityservice",
            "android.accounts",
            "android.animation",
            "android.annotation",
            "android.app",
            "android.app.admin",
            "android.app.assist",
            "android.app.backup",
            "android.app.job",
            "android.app.usage",
            "android.appwidget",
            "android.bluetooth",
            "android.bluetooth.le",
            "android.content",
            "android.content.pm",
            "android.content.res",
            "android.database",
            "android.database.sqlite",
            "android.databinding",
            "android.drm",
            "android.gesture",
            "android.graphics",
            "android.graphics.drawable",
            "android.graphics.drawable.shapes",
            "android.graphics.pdf",
            "android.hardware",
            "android.hardware.camera2",
            "android.hardware.camera2.params",
            "android.hardware.display",
            "android.hardware.fingerprint",
            "android.hardware.input",
            "android.hardware.usb",
            "android.inputmethodservice",
            "android.location",
            "android.media",
            "android.media.audiofx",
            "android.media.browse",
            "android.media.effect",
            "android.media.midi",
            "android.media.projection",
            "android.media.session",
            "android.media.tv",
            "android.mtp",
            "android.net",
            "android.net.http",
            "android.net.nsd",
            "android.net.rtp",
            "android.net.sip",
            "android.net.wifi",
            "android.net.wifi.p2p",
            "android.net.wifi.p2p.nsd",
            "android.nfc",
            "android.nfc.cardemulation",
            "android.nfc.tech",
            "android.opengl",
            "android.os",
            "android.os.storage",
            "android.preference",
            "android.print",
            "android.print.pdf",
            "android.printservice",
            "android.provider",
            "android.renderscript",
            "android.sax",
            "android.security",
            "android.security.keystore",
            "android.service.carrier",
            "android.service.chooser",
            "android.service.dreams",
            "android.service.media",
            "android.service.notification",
            "android.service.restrictions",
            "android.service.textservice",
            "android.service.voice",
            "android.service.wallpaper",
            "android.speech",
            "android.speech.tts",
            "android.support.annotation",
            "android.support.app.recommendation",
            "android.support.customtabs",
            "android.support.design",
            "android.support.design.widget",
            "android.support.multidex",
            "android.support.percent",
            "android.support.v13.app",
            "android.support.v14.preference",
            "android.support.v17.leanback",
            "android.support.v17.leanback.app",
            "android.support.v17.leanback.database",
            "android.support.v17.leanback.graphics",
            "android.support.v17.leanback.system",
            "android.support.v17.leanback.widget",
            "android.support.v17.preference",
            "android.support.v4.accessibilityservice",
            "android.support.v4.animation",
            "android.support.v4.app",
            "android.support.v4.content",
            "android.support.v4.content.pm",
            "android.support.v4.content.res",
            "android.support.v4.database",
            "android.support.v4.graphics",
            "android.support.v4.graphics.drawable",
            "android.support.v4.hardware.display",
            "android.support.v4.hardware.fingerprint",
            "android.support.v4.media",
            "android.support.v4.media.session",
            "android.support.v4.net",
            "android.support.v4.os",
            "android.support.v4.print",
            "android.support.v4.provider",
            "android.support.v4.text",
            "android.support.v4.util",
            "android.support.v4.view",
            "android.support.v4.view.accessibility",
            "android.support.v4.view.animation",
            "android.support.v4.widget",
            "android.support.v7.app",
            "android.support.v7.appcompat",
            "android.support.v7.cardview",
            "android.support.v7.graphics",
            "android.support.v7.graphics.drawable",
            "android.support.v7.gridlayout",
            "android.support.v7.media",
            "android.support.v7.mediarouter",
            "android.support.v7.preference",
            "android.support.v7.recyclerview",
            "android.support.v7.util",
            "android.support.v7.view",
            "android.support.v7.widget",
            "android.support.v7.widget.helper",
            "android.support.v7.widget.util",
            "android.support.v8.renderscript",
            "android.system",
            "android.telecom",
            "android.telephony",
            "android.telephony.cdma",
            "android.telephony.gsm",
            "android.test",
            "android.test.mock",
            "android.test.suitebuilder",
            "android.test.suitebuilder.annotation",
            "android.text",
            "android.text.format",
            "android.text.method",
            "android.text.style",
            "android.text.util",
            "android.transition",
            "android.util",
            "android.view",
            "android.view.accessibility",
            "android.view.animation",
            "android.view.inputmethod",
            "android.view.textservice",
            "android.webkit",
            "android.widget",
            "com.android.internal.backup",
            "com.android.internal.logging",
            "com.android.internal.os",
            "com.android.internal.statusbar",
            "com.android.internal.widget",
            "com.android.test.runner",
            "dalvik.annotation",
            "dalvik.bytecode",
            "dalvik.system",
            "java.awt.font",
            "java.beans",
            "java.io",
            "java.lang",
            "java.lang.annotation",
            "java.lang.ref",
            "java.lang.reflect",
            "java.math",
            "java.net",
            "java.nio",
            "java.nio.channels",
            "java.nio.channels.spi",
            "java.nio.charset",
            "java.nio.charset.spi",
            "java.security",
            "java.security.acl",
            "java.security.cert",
            "java.security.interfaces",
            "java.security.spec",
            "java.sql",
            "java.text",
            "java.util",
            "java.util.concurrent",
            "java.util.concurrent.atomic",
            "java.util.concurrent.locks",
            "java.util.jar",
            "java.util.logging",
            "java.util.prefs",
            "java.util.regex",
            "java.util.zip",
            "javax.crypto",
            "javax.crypto.interfaces",
            "javax.crypto.spec",
            "javax.microedition.khronos.egl",
            "javax.microedition.khronos.opengles",
            "javax.net",
            "javax.net.ssl",
            "javax.security.auth",
            "javax.security.auth.callback",
            "javax.security.auth.login",
            "javax.security.auth.x500",
            "javax.security.cert",
            "javax.sql",
            "javax.xml",
            "javax.xml.datatype",
            "javax.xml.namespace",
            "javax.xml.parsers",
            "javax.xml.transform",
            "javax.xml.transform.dom",
            "javax.xml.transform.sax",
            "javax.xml.transform.stream",
            "javax.xml.validation",
            "javax.xml.xpath",
            "junit.framework",
            "junit.runner",
            "org.apache.http.conn",
            "org.apache.http.conn.scheme",
            "org.apache.http.conn.ssl",
            "org.apache.http.params",
            "org.json",
            "org.w3c.dom",
            "org.w3c.dom.ls",
            "org.xml.sax",
            "org.xml.sax.ext",
            "org.xml.sax.helpers",
            "org.xmlpull.v1",
            "org.xmlpull.v1.sax2"]


def startWithAny(called):
    for api in API_LIST:
        if called.startswith(api):
            return True
    return False

def getDictClass(callGraphFile, restriction):
    res = {}
    with open(callGraphFile) as data_file:
            datas = data_file.readlines()
            for data in datas:
                data = data.strip()
                if data[:2] == "C:":
                    data = data[2:]
                    caller, called = data.split()
                    if startWithAny(called) and restriction in caller:
                        if caller in res:
                            res[caller].append(called)
                        else:
                            res[caller] = [called]

    return res

def getClassSize(callGraphFile, restriction):
    res = {}
    alreadyConcerned = []
    with open(callGraphFile) as data_file:
            datas = data_file.readlines()
            for data in datas:
                data = data.strip()
                if data[:2] == "M:":
                    data = data[2:]
                    caller, called = data.split()
                    called = called[3:]
                    klass, method = caller.split(":")
                    klass = klass.split(".")[-1]
                    if restriction in caller:
                        if "$" in klass:
                            klass = klass.split("$")[0]
                        if not [klass,method] in alreadyConcerned:
                            if klass in res:
                                res[klass] +=1
                            else:
                                res[klass] =1
                            alreadyConcerned.append([klass,method])

    return res


def scoreApiCall(callgraphPath, packageName):
    graph = getDictClass(callgraphPath, packageName)

    res = {}
    for i in graph:
        caller = i.split(".")[-1].split("$")[0] if "$" in i.split(".")[-1] else i.split(".")[-1]
        if caller in res:
            res[caller] += len(graph[i])
        else:
            res[caller] = len(graph[i])
    return res


def scoreClassSize(callgraphPath, packageName):
    res = getClassSize(callgraphPath, packageName)
    return res




if __name__ == '__main__':
    main()