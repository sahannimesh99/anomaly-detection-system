package org.sahan.repository;

import org.sahan.entity.Payment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PaymentRepository extends JpaRepository<Payment, Long> {
    Page<Payment> findByAnomalyTrue(Pageable pageable);
    Page<Payment> findByAnomalyFalse(Pageable pageable);
    Page<Payment> findBySeverity(String severity, Pageable pageable);
}
