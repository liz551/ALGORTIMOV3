package pe.edu.upc.repository;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import pe.edu.upc.model.Paciente;
@Repository
public interface IPacienteDAO extends JpaRepository<Paciente, Integer> {
	@Query("from Paciente g where g.nroDocumento like %:nroDocumento%")
	List<Paciente> buscarPaciente(@Param("nroDocumento")String nroDocumento);
}
