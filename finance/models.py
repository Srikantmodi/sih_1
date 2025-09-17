from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class FinancialLedgerEntry(models.Model):
    """Financial ledger for tracking farm income and expenses"""
    
    ENTRY_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    INCOME_CATEGORIES = [
        ('crop_sale', 'Crop Sale'),
        ('livestock_sale', 'Livestock Sale'),
        ('dairy_products', 'Dairy Products'),
        ('government_subsidy', 'Government Subsidy'),
        ('loan', 'Loan'),
        ('other_income', 'Other Income'),
    ]
    
    EXPENSE_CATEGORIES = [
        ('seeds', 'Seeds'),
        ('fertilizer', 'Fertilizer'),
        ('pesticides', 'Pesticides'),
        ('fuel', 'Fuel'),
        ('labor', 'Labor'),
        ('machinery', 'Machinery'),
        ('irrigation', 'Irrigation'),
        ('transportation', 'Transportation'),
        ('loan_repayment', 'Loan Repayment'),
        ('insurance', 'Insurance'),
        ('other_expense', 'Other Expense'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ledger_entries')
    date = models.DateField(help_text="Date of the transaction")
    entry_type = models.CharField(
        max_length=10, 
        choices=ENTRY_TYPES,
        help_text="Type of financial entry"
    )
    amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Transaction amount in INR"
    )
    description = models.CharField(
        max_length=200, 
        help_text="Brief description of the transaction"
    )
    category = models.CharField(
        max_length=50,
        help_text="Category of income or expense"
    )
    crop_related = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Specific crop this transaction relates to"
    )
    payment_method = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        choices=[
            ('cash', 'Cash'),
            ('bank_transfer', 'Bank Transfer'),
            ('cheque', 'Cheque'),
            ('upi', 'UPI'),
            ('other', 'Other'),
        ],
        help_text="Method of payment"
    )
    reference_number = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Transaction reference number (optional)"
    )
    notes = models.TextField(
        blank=True, 
        null=True,
        help_text="Additional notes about the transaction"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.entry_type} ₹{self.amount} on {self.date}"
    
    @property
    def signed_amount(self):
        """Return amount with appropriate sign for calculations"""
        return self.amount if self.entry_type == 'income' else -self.amount
    
    class Meta:
        verbose_name = "Financial Ledger Entry"
        verbose_name_plural = "Financial Ledger Entries"
        ordering = ['-date', '-created_at']
