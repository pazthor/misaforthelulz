package com.journaler.activity

import com.journaler.Journaler
import com.journaler.R

class MainActivity : BaseActivity() {
    override val tag = "Main.Activity"
    override fun getLayout() = R.layout.activity_main
    override fun getActivityTittle() =R.string.app_name
}