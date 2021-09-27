package pe.edu.upc.model;

import java.io.Serializable;

import javax.persistence.*;
import javax.validation.constraints.NotNull;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Data;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;


@Data
@Entity
@Table(name ="emergency")
public class Emergency {

private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private int id;

	@NotNull
	@Column(name = "state", length = 15, nullable = false)
	private int state;

	@NotNull
	@Column(name = "heart_rate", nullable = false)
	private int heartRate;

	@NotNull
	@Column(name = "lenght", nullable = false)
	private String length;

	@NotNull
	@Column(name = "latitude", nullable = false)
	private String latitude;


	@ManyToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "patient_id", nullable = false)
	@OnDelete(action = OnDeleteAction.CASCADE)
	@JsonIgnore
	private MovPatient patient;


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


	public MovPatient getPatient() {
		return patient;
	}


	public void setPatient(MovPatient patient) {
		this.patient = patient;
	}
	
	
	
}