package com.journaler.fragment
import com.journaler.R

class ItemsFragment : BaseFragment() {
    override val logTag = "Items Fragment"
    override fun getLayout(): Int{
        return R.layout.fragment_items
    }
}