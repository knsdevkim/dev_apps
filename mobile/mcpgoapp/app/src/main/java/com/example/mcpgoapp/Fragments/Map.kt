package com.example.mcpgoapp.Fragments

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.example.mcpgoapp.Authenticate.Authenticate
import com.example.mcpgoapp.Handlers.MapHandlers
import com.example.mcpgoapp.Models.McpModel
import com.example.mcpgoapp.R
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.MapView
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.Marker
import com.google.android.gms.maps.model.MarkerOptions
import com.google.gson.Gson
import io.realm.Realm
import io.realm.kotlin.where
import org.json.JSONArray

class Map: Fragment(), OnMapReadyCallback, GoogleMap.OnInfoWindowClickListener {

    private lateinit var realm: Realm

    private lateinit var mapView: MapView

    private val markerInfo: HashMap<String, String> = HashMap<String, String>()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val root: View = inflater.inflate(R.layout.map, container, false)
        this.run(root)
        this.mapView.onCreate(savedInstanceState)
        return root
    }
    
    companion object {
        private const val TAG = "Map"
    }

    override fun onMapReady(googleMap: GoogleMap?) {
        googleMap?.apply {
            realm = Realm.getDefaultInstance()
            val mcpdata  = realm.where<McpModel>()
                .equalTo("salesperson", arguments!!.getString("salesperson"))
                .distinct("customer")
                .findAllAsync()!!

            val jsonData = Gson().toJson(realm.copyFromRealm(mcpdata))
            try {
                val jsonArray = JSONArray(jsonData)

                val mapCollection: ArrayList<MapHandlers> = ArrayList<MapHandlers>()

                for (i in 0 until jsonArray.length()) {
                    val dataObject  = jsonArray.getJSONObject(i)
                    val geolocation = dataObject.getString("geolocation").split(",")
                    mapCollection.add(MapHandlers(
                        geolocation[0].toDouble(),
                        geolocation[1].toDouble(),
                        dataObject.getString("customer"),
                        dataObject.getString("id")
                    ))
                }

                mapCollection.forEach { markerData ->
                    val marker = addMarker(MarkerOptions()
                        .position(LatLng(markerData.latitude, markerData.longitude))
                        .title(markerData.title))
                    markerInfo[marker.id] = markerData.id
                }

                val map_camera_focus = LatLng(10.0202564, 122.4102503)

                moveCamera(CameraUpdateFactory.newLatLng(map_camera_focus))
                animateCamera(CameraUpdateFactory.newLatLngZoom(map_camera_focus, 7.0f))

            } catch(e: Exception) {
                e.message?.let { error ->
                    Log.e(TAG, error)
                }
            }
        }

        googleMap?.setOnInfoWindowClickListener(this)
    }

    override fun onInfoWindowClick(marker: Marker?) {
        this.markerInfo[marker!!.id]?.let { info ->
            val fragment = CustomerDetails()

            val bundle = Bundle()
            bundle.putString("id", info)

            val fragmentManager     = activity!!.supportFragmentManager
            val fragmentTransaction = fragmentManager.beginTransaction()

            fragment.arguments = bundle

            fragmentTransaction.replace(R.id.flFragment, fragment)
            fragmentTransaction.addToBackStack(null)
            fragmentTransaction.commit()
        }
    }

    override fun onDestroy() {
        this.mapView.onDestroy()
        super.onDestroy()
        this.realm.close()
    }

    override fun onResume() {
        this.mapView.onResume()
        super.onResume()
    }

    override fun onPause() {
        this.mapView.onPause()
        super.onPause()
    }

    override fun onLowMemory() {
        this.mapView.onLowMemory()
        super.onLowMemory()
    }

    private fun run(v: View) {
        Authenticate(activity!!).not_authenticated()
        this.initializeWidgets(v)
    }

    private fun initializeWidgets(v: View) {
        this.mapView = v.findViewById(R.id.mapView)
        this.mapView.getMapAsync(this)
    }
}