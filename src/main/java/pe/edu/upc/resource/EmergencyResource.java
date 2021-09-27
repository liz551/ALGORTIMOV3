package pe.edu.upc.resource;

import lombok.Data;

import javax.persistence.Column;
import javax.validation.constraints.NotNull;

@Data
public class EmergencyResource {

    private int id;
    private int state;
    private int heartRate;
    private String length;
    private String latitude;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getState() {
		return state;
	}
	public void setState(int state) {
		this.state = state;
	}
	public int getHeartRate() {
		return heartRate;
	}
	public void setHeartRate(int heartRate) {
		this.heartRate = heartRate;
	}
	public String getLength() {
		return length;
	}
	public void setLength(String length) {
		this.length = length;
	}
	public String getLatitude() {
		return latitude;
	}
	public void setLatitude(String latitude) {
		this.latitude = latitude;
	}
    
    

}
