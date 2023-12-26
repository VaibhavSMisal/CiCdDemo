package com.example.cicddemoapp

import android.view.View
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.isDisplayed
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.espresso.matcher.ViewMatchers.withText
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.ext.junit.runners.AndroidJUnit4

import org.junit.Test
import org.junit.runner.RunWith
import java.io.BufferedReader
import java.io.InputStreamReader

import org.junit.Assert.*
import org.junit.Before
import org.junit.Rule

/**
 * Instrumented test, which will execute on an Android device.
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
@RunWith(AndroidJUnit4::class)
class ExampleInstrumentedTest {

    @Rule
    @JvmField
    var activityRule = ActivityScenarioRule(MainActivity::class.java)
    private var decorView: View? = null

    @Before
    fun setUp() {
        activityRule.scenario.onActivity { activity: MainActivity -> decorView = activity.window.decorView }
    }
    @Test
    fun test1() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.cicddemoapp", appContext.packageName)

        val process = Runtime.getRuntime().exec("du -sh /data/data/com.example.cicddemoapp/cache")
        process.waitFor()
        val bufferedReader = BufferedReader(InputStreamReader(process.inputStream))
        println("### CacheSize: First = ${bufferedReader.readLine()}")
    }

    @Test
    fun test2() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.cicddemoapp", appContext.packageName)

        onView(withId(R.id.button)).check(matches(isDisplayed())).perform(click())
        val process = Runtime.getRuntime().exec("du -sh /data/data/com.example.cicddemoapp/cache")
        process.waitFor()
        val bufferedReader = BufferedReader(InputStreamReader(process.inputStream))
        println("### CacheSize: Second = ${bufferedReader.readLine()}")
    }

    @Test
    fun test3() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.cicddemoapp", appContext.packageName)

        onView(withText("Hello World!")).check(matches(isDisplayed()))
        onView(withId(R.id.button)).check(matches(isDisplayed())).perform(click())
        onView(withText(R.string.text_changed_on_click)).check(matches(isDisplayed()))
        val process = Runtime.getRuntime().exec("du -sh /data/data/com.example.cicddemoapp/cache")
        process.waitFor()
        val bufferedReader = BufferedReader(InputStreamReader(process.inputStream))
        println("### CacheSize: Third = ${bufferedReader.readLine()}")
    }
}
