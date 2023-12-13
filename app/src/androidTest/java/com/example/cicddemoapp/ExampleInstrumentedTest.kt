package com.example.cicddemoapp

import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.ext.junit.runners.AndroidJUnit4

import org.junit.Test
import org.junit.runner.RunWith
import java.io.BufferedReader
import java.io.InputStreamReader

import org.junit.Assert.*

/**
 * Instrumented test, which will execute on an Android device.
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
@RunWith(AndroidJUnit4::class)
class ExampleInstrumentedTest {
    @Test
    fun useAppContext() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.cicddemoapp", appContext.packageName)

        val process = Runtime.getRuntime().exec("du -sh /data/data/com.example.cicddemoapp/cache")
        process.waitFor()
        val bufferedReader = BufferedReader(InputStreamreader(process.inputStream))
        println("### Cache size = ${bufferedReader.readLine()})
    }
}
