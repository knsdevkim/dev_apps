package com.example.mcpgoapp.Fragments

import android.Manifest
import android.app.AlertDialog
import android.content.DialogInterface
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.core.app.ActivityCompat
import androidx.fragment.app.Fragment
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.example.mcpgoapp.Utils.ModelController
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.MapView
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import io.realm.Realm
import io.realm.kotlin.where
import java.math.RoundingMode
import java.text.DecimalFormat


class CustomerDetails: Fragment(), OnMapReadyCallback, View.OnClickListener {

    private lateinit var realm: Realm

    private lateinit var customername: TextView
    private lateinit var address: TextView
    private lateinit var gtm: TextView
    private lateinit var salesperson: TextView
    private lateinit var channel: TextView
    private lateinit var freq: TextView
    private lateinit var odd_even: TextView
    private lateinit var ave_nps: TextView
    private lateinit var c_term: TextView
    private lateinit var c_limit: TextView
    private lateinit var mapView: MapView

    private lateinit var dial: ImageView

    private lateinit var map_customername: String
    private lateinit var latLng: LatLng

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val root: View = inflater.inflate(R.layout.customerdetails, container, false)
        this.run(root)
        this.mapView.onCreate(savedInstanceState)
        return root
    }

    override fun onMapReady(googleMap: GoogleMap?) {
        googleMap?.apply {
            val marker_target = latLng
            addMarker(
                MarkerOptions()
                    .position(marker_target)
                    .title(map_customername)
            )
            moveCamera(CameraUpdateFactory.newLatLng(marker_target))
            animateCamera(CameraUpdateFactory.newLatLngZoom(marker_target, 15.0f))
        }
    }

    override fun onPause() {
        mapView.onPause()
        super.onPause()
    }

    override fun onLowMemory() {
        mapView.onLowMemory()
        super.onLowMemory()
    }

    override fun onResume() {
        mapView.onResume()
        super.onResume()
    }

    override fun onDestroy() {
        mapView.onDestroy()
        super.onDestroy()
        this.realm.close()
    }

    override fun onClick(v: View?) {
        when(v) {
            dial -> {
                val alertDialog: AlertDialog.Builder = AlertDialog.Builder(activity!!)

                alertDialog.setTitle("Attempt to call ...")
                alertDialog.setMessage("This may apply data charges on your sim, Continue?")
                alertDialog.setPositiveButton("Yes, Call") { _: DialogInterface, _: Int ->
                    startActivity(Intent(Intent.ACTION_CALL, Uri.parse("tel: 09215536439")))
                }
                alertDialog.setNegativeButton("Cancel") { _: DialogInterface, _: Int ->
                    // CANCEL
                }

                val showAlertCallDialog = alertDialog.create()
                showAlertCallDialog.show()
            }
        }
    }

    companion object {
        private const val TAG = "CustomerDetails"
    }

    private fun run(v: View) {
        this.loadWidgets(v)
        this.pullData()
        mapView.getMapAsync(this)
    }

    private fun loadWidgets(v: View) {
        customername = v.findViewById(R.id.customername)
        address      = v.findViewById(R.id.address)
        gtm          = v.findViewById(R.id.gtm)
        salesperson  = v.findViewById(R.id.salesperson)
        channel      = v.findViewById(R.id.channel)
        freq         = v.findViewById(R.id.freq)
        odd_even     = v.findViewById(R.id.odd_even)
        ave_nps      = v.findViewById(R.id.ave_nps)
        c_term       = v.findViewById(R.id.c_term)
        c_limit      = v.findViewById(R.id.c_limit)
        mapView      = v.findViewById(R.id.mapView)
        dial         = v.findViewById(R.id.dialIcon)

        dial.setOnClickListener(this)
    }

    private fun pullData() {
        try {
            this.realm = ModelController().modelInstance()

            val data = this.realm.where<McpModel>()
                .equalTo("id", arguments!!.getString("id")!!.toInt())
                .findFirst()!!

            val decimalFormat = DecimalFormat("#,###.##")
            decimalFormat.roundingMode = RoundingMode.CEILING

            this.customername.text = data.customer
            this.address.text      = data.address
            this.gtm.text          = data.gtm
            this.salesperson.text  = data.salesperson
            this.channel.text      = data.channel
            this.freq.text         = data.freq
            this.odd_even.text     = if (data.odd_even != "null") data.odd_even else "0"
            this.ave_nps.text      = decimalFormat.format(data.ave_nps.toDouble())
            this.c_term.text       = if (data.cterm != "null") data.cterm else "0"
            this.c_limit.text      = if (data.climit != "null") data.climit else "0"

            val fetchGeolocation = data.geolocation.split(",")
            this.map_customername = data.customer
            this.latLng = LatLng(fetchGeolocation[0].toDouble(), fetchGeolocation[1].toDouble())

        } catch (e: Exception) {
            e.message?.let { message ->
                Log.e(TAG, message)
            }
        } finally {
            this.realm.close()
        }
    }
}