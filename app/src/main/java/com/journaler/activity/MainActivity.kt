package com.journaler.activity

import android.os.Bundle
import com.journaler.Journaler
import com.journaler.R
import com.journaler.fragment.ItemsFragment

class MainActivity : BaseActivity() {
    override val tag = "Main Activity"
    override fun getLayout() = R.layout.activity_main
    override fun getActivityTittle() =R.string.app_name

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val fragment = ItemsFragment()
        supportFragmentManager
                .beginTransaction()
                .add(R.id.fragment_container, fragment)
                .commit()
    }
}