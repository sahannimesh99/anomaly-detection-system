package org.sahan.repository;

import org.sahan.entity.Payment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PaymentRepository extends JpaRepository<Payment, Long> {
    Page<Payment> findByAnomalyTrue(Pageable pageable);
    Page<Payment> findByAnomalyFalse(Pageable pageable);
    Page<Payment> findBySeverity(String severity, Pageable pageable);
    List<Payment> findByOrderId(Long orderId);
}
