package com.journaler.activity

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.journaler.R

class TodoActivity : ItemActivity() {
    override val tag = "Todo.Activity"
    override fun getLayout() = R.layout.activity_todo
    override fun getActivityTittle() = R.string.app_name
}
