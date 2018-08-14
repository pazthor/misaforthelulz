package com.journaler.activity

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.journaler.R

open class ItemActivity : BaseActivity() {

    override val tag = "Item.Activity"
    override fun getLayout() = R.layout.activity_item
    override fun getActivityTittle() = R.string.app_name

//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//        setContentView(R.layout.activity_item)
//    }
}
