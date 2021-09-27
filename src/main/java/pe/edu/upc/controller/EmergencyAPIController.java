package pe.edu.upc.controller;

import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import pe.edu.upc.model.Emergency;
import pe.edu.upc.model.MovPatient;
import pe.edu.upc.model.Paciente;
import pe.edu.upc.resource.EmergencyResource;
import pe.edu.upc.resource.MovPatientResource;
import pe.edu.upc.resource.SaveEmergencyResource;
import pe.edu.upc.resource.SaveMovPatientResource;
import pe.edu.upc.service.EmergencyService;

import javax.validation.Valid;
import java.text.ParseException;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@RestController
@CrossOrigin
@RequestMapping("/api")
public class EmergencyAPIController {

    @Autowired
    private ModelMapper mapper;

    @Autowired
    private EmergencyService emergencyService;

    @PostMapping("/mobile/{mobileId}/emergencies")
    public EmergencyResource createEmergency(@PathVariable(name = "mobileId") int mobileId, @Valid @RequestBody SaveEmergencyResource resource) {
        return convertToResource(emergencyService.createEmergency(mobileId, convertToEntity(resource)));
    }

    @GetMapping("/mobile/{mobileId}/emergencies")
    public Page<EmergencyResource> getAllEmergenciesByPatientId(@PathVariable(name = "mobileId") int mobileId, Pageable pageable) {
        Page<Emergency> emergencyPage = emergencyService.getAllEmergenciesByPatientId(mobileId, pageable);
        List<EmergencyResource> resources = emergencyPage.getContent().stream().map(this::convertToResource).collect(Collectors.toList());
        return new PageImpl<>(resources, pageable, resources.size());
    }

    @GetMapping("/mobile/{mobileId}/emergencies/{emergencyId}")
    public EmergencyResource getEmergencyByIdAndPatientId(@PathVariable(name = "mobileId") int mobileId, @PathVariable(name = "emergencyId") int emergencyId) {
        return convertToResource(emergencyService.getEmergencyByIdAndPatientId(mobileId, emergencyId));
    }


    @PutMapping("/mobile/{mobileId}/emergencies/update/{emergencyId}")
    public EmergencyResource updateEmergency(@PathVariable(name = "mobileId") int mobileId, @PathVariable(name = "emergencyId") int emergencyId, @Valid @RequestBody SaveEmergencyResource resource) {
        return convertToResource(emergencyService.updateEmergency(mobileId, emergencyId, convertToEntity(resource)));
    }








    private Emergency convertToEntity(SaveEmergencyResource resource){
        return mapper.map(resource, Emergency.class);
    }

    private EmergencyResource convertToResource(Emergency entity){
        return mapper.map(entity, EmergencyResource.class);
    }


}
