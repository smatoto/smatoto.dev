document.addEventListener('DOMContentLoaded', function() {
  // Inject profile section into nav on home page only
  // Check if we're on home page by looking for featured-grid (only on home page)
  const featuredGrid = document.querySelector('.featured-grid');

  if (featuredGrid) {
    const navElement = document.querySelector('.md-nav');
    if (navElement) {
      const profileHTML = `
        <div style="padding: 1rem; text-align: left; border-bottom: 1px solid var(--md-default-fg-color--lighter); margin-bottom: 1rem; display: flex; gap: 0.75rem; align-items: flex-start;">
          <img src="https://github.com/smatoto.png" alt="Sermil Matoto" style="width: 60px; height: 60px; border-radius: 50%; flex-shrink: 0;">
          <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
            <p style="margin: 0; font-weight: 600; font-size: 0.8rem; line-height: 1.2;">Sermil Matoto</p>
            <p style="margin: 0.2rem 0 0 0; font-size: 0.7rem; color: var(--md-default-fg-color--light);">GDE, Cloud</p>
          </div>
        </div>
      `;
      navElement.insertAdjacentHTML('afterbegin', profileHTML);
    }
  }

  const filters = { year: 'all', category: 'all', type: 'all' };

  // Add click handlers to all filter buttons
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const group = this.dataset.group;
      const value = this.dataset.value;

      // Remove active class from all buttons in this group
      document.querySelectorAll(`.filter-btn[data-group="${group}"]`)
        .forEach(b => b.classList.remove('active'));

      // Add active class to clicked button
      this.classList.add('active');

      // Update filter state
      filters[group] = value;

      // Show/hide cards based on all active filters
      document.querySelectorAll('.session-card[data-year]').forEach(card => {
        const matchYear = filters.year === 'all' || card.dataset.year === filters.year;
        const matchCategory = filters.category === 'all' || card.dataset.category === filters.category;
        const matchType = filters.type === 'all' || card.dataset.type === filters.type;

        const show = matchYear && matchCategory && matchType;
        card.classList.toggle('hidden', !show);
      });
    });
  });

  // Set initial active state for "All" buttons
  document.querySelectorAll('.filter-btn[data-value="all"]').forEach(btn => {
    btn.classList.add('active');
  });

  // Expand the latest 2 years (2026, 2025) in navigation by default
  setTimeout(() => {
    document.querySelectorAll('.md-nav__label').forEach(label => {
      const text = label.textContent.trim();
      if (text === '2026' || text === '2025') {
        const checkbox = label.previousElementSibling;
        if (checkbox && checkbox.type === 'checkbox') {
          checkbox.checked = true;
        }
      }
    });
  }, 100);

  // Check for expired certifications and add expired class
  const today = new Date().toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
  document.querySelectorAll('.cert-card[data-expires]').forEach(card => {
    const expiresStr = card.getAttribute('data-expires');
    // Compare as strings to avoid timezone issues
    if (today > expiresStr) {
      card.classList.add('expired');
    }
  });
});
